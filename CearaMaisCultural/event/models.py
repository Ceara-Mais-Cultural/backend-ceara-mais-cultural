from django.db import models

from project.models import Project
from city.models import City


class Event(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-datetime"]
