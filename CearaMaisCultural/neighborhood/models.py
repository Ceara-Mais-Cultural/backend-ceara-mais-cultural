from django.db import models

from city.models import City


class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(
        City,
        related_name="city",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"
        ordering = ["name"]
