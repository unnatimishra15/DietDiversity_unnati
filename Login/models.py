from django.db import models
from wagtail.core.models import Page
# Create your models here.

class LoginFormPage(Page):

    template = "Login.html"
    
class LoginModel(models.Model):
        Username = models.CharField(max_length=100)
        Password= models.CharField(max_length=100)