from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class Account(AbstractUser):
    ROLE_CHOICES = (
        (1, "Admin"),
        (2, "Teacher"),
        (3, "Student")
    )
    username = None
    passport_number = models.CharField(max_length=10, unique=True, null=True)
    phone = models.CharField(max_length=30, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
