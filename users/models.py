from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

# Create your models here.

class UserType(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=True)
