from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MaxLengthValidator, EmailValidator, RegexValidator
from django.db import models

from neighborhood.models import Neighborhood
from city.models import City


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$", message="CPF inválido"
            )
        ],
    )
    full_name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    email = models.EmailField(validators=[], unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=1)
    community = models.TextField(validators=[MaxLengthValidator(100)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        role = (
            "Comissão"
            if self.is_superuser
            else "Mobilizador" if self.is_staff else "Agente Cultural"
        )
        return self.full_name + " - " + role

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["full_name"]
