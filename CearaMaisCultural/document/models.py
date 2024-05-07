from django.db import models

from project.models import Project

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to='document/files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)