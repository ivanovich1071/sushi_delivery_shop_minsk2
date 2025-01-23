from django.db import models

# Create your models here.
# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telegram_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
