from django.db import models
from django.forms import ValidationError
from city.models import City
from neighborhood.models import Neighborhood
from user.models import User
from category.models import Category
from django.core.validators import MaxLengthValidator

PROJECT_ANALYSIS_STATUS = [
    ("pending", "Pendente"),
    ("approved", "Aprovado"),
    ("declined", "Recusado"),
    ("waiting", "Esperando Documentação"),
]

VOTING_OPTIONS = [
    ("approved", "Aprovado"),
    ("declined", "Recusado"),
]


class Project(models.Model):
    title = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    author = models.ForeignKey(
        User,
        related_name="author",
        on_delete=models.CASCADE,
        limit_choices_to={"is_staff": False},
    )
    promoter = models.ForeignKey(
        User,
        related_name="promoter",
        on_delete=models.CASCADE,
        limit_choices_to={"is_staff": True, "is_superuser": False},
        null=True,
    )
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=1)
    community = models.TextField(validators=[MaxLengthValidator(100)], null=True)
    location = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    file = models.FileField(upload_to="documents/", blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=8, choices=PROJECT_ANALYSIS_STATUS, default="waiting"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["status", "-created_at"]

    def calculate_status(self):
        total_superusers = User.objects.filter(is_superuser=True).count()
        votes = ProjectVote.objects.filter(project=self)
        approval_votes = votes.filter(vote="approved").count()
        decline_votes = votes.filter(vote="declined").count()

        if votes.count() >= total_superusers - 1: # Menos um por causa da conta do desenvolvedor
            if approval_votes > decline_votes:
                self.status = "approved"
            else:
                self.status = "declined"
            self.save()
            self.decline_excess_approved_projects()
        else:
            self.status = "pending"

    def decline_excess_approved_projects(self):
        approved_projects = Project.objects.filter(
            city=self.city, status="approved"
        ).order_by("created_at")

        if approved_projects.count() > 40:
            excess_projects = approved_projects[40:]
            excess_projects.update(status="declined")

    def clean(self):
        approved_projects_count = Project.objects.filter(
            city=self.city, status="approved"
        ).count()
        if self.status == "approved" and approved_projects_count >= 40:
            raise ValidationError(
                "Não é possível aprovar mais projetos nesta cidade. O limite de 40 projetos aprovados já foi atingido."
            )


class ProjectVote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        limit_choices_to={"is_staff": True, "is_superuser": True},
        on_delete=models.CASCADE,
    )
    vote = models.CharField(max_length=20, choices=VOTING_OPTIONS)

    class Meta:
        unique_together = ("project", "user")

    def save(self, *args, **kwargs):
        if ProjectVote.objects.filter(project=self.project, user=self.user).exists():
            raise ValidationError("O usuário já votou neste projeto")

        approved_projects_count = Project.objects.filter(
            city=self.project.city, status="approved"
        ).count()
        if approved_projects_count >= 40:
            raise ValidationError(
                "Não é possível votar. O limite de 40 projetos aprovados nesta cidade já foi atingido."
            )

        super(ProjectVote, self).save(*args, **kwargs)
        self.project.calculate_status()

    def delete(self, *args, **kwargs):
        super(ProjectVote, self).delete(*args, **kwargs)
        self.project.calculate_status()
