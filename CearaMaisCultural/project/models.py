from django.db import models
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
        limit_choices_to={"is_staff": True, 'is_superuser': False},
        null=True,
    )
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=1)
    community = models.TextField(validators=[MaxLengthValidator(100)], null=True)
    location = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=8, choices=PROJECT_ANALYSIS_STATUS, default="pending"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["status", "-created_at"]
