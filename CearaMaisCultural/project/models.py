from django.db import models
from customUser.models import CustomUser
from category.models import Category
from django.core.validators import MaxLengthValidator, EmailValidator

class Project(models.Model):
    title = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    promoter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    description = models.TextField()
    location = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title