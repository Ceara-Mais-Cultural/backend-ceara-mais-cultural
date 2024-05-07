from django.db import models
from category.models import Category
from user.models import CustomUser
from django.core.validators import MaxLengthValidator

class Project(models.Model):
    title = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title