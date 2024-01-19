from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')

    age = models.PositiveIntegerField(**NULLABLE, verbose_name='лет')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=30, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
