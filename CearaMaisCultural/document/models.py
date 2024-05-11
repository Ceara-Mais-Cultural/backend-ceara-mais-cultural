from django.db import models

from project.models import Project


class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to="document/files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return f"{self.project.title} - {self.name}"
        else:
            return f"{self.project.title} - {self.file.name}"

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["-uploaded_at"]
