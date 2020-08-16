from django.db import models
from wagtail.core.models import Page
# Create your models here.


class SchoolPage(Page):

    template = "schoolregistration.html"
    
class SchoolModel(models.Model):
        objects = models.Manager() 
        SchoolID= models.IntegerField()
        SchoolName  = models.CharField(max_length= 200)
        CoordinatorId  = models.IntegerField()
        