from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxLengthValidator, EmailValidator, RegexValidator
from django.db import models

from city.models import City

class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, email, cpf, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(full_name=full_name, email=email, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(full_name, email, cpf, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    cpf = models.CharField(max_length=14, validators=[RegexValidator(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', message='CPF inválido')])
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'cpf']

    def __str__(self):
        return self.email
