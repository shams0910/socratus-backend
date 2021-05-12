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
    middle_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField()
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
