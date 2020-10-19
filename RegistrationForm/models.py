from django.db import models
from wagtail.core.models import Page
# Create your models here.

gender = [
    ('male', 'Male'),
    ('female', 'Female'),
 ]

spendday = [
    ('sleeping','Sleeping'),
    ('eating','Eating'),
    ('studying','Studying'),
    ('siting and working at a desk','Sitting and working at a desk'),
    ('sports training','Sports Training'),
    ('siting in front of the TV','Sitting in front of the TV'),
    ('sitind at the computer','Sitting at the computer'),
    ('playing outside','Playing outside'),
    ('running','Running'),
    ('zumba','Zumba'),
    ('aerobics','Aerobics'),
    ('briskwalking',' Brisk walking'),
    ('yoga','Yoga'),
    ('meditation','Meditation'),
]


class RegistrationFormPage(Page):

    template = "register.html"
    
class RegisterationFormModel(models.Model):
        Name= models.CharField(max_length=100)
        Age = models.IntegerField(default= 0)
        Gender= models.CharField(choices=gender,max_length= 20,default='Male')
        StudentClass  = models.CharField(max_length=100 ,default='0')
        SpendingDay =  models.CharField(choices= spendday,max_length= 100 ,default= 'Sleeping')
        Height = models.IntegerField(default=0)
        Weight = models.IntegerField(default=0)
        Waist = models.IntegerField(default=0)
        Hip = models.IntegerField()
        objects = models.Manager()