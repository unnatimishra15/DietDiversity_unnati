from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


CHOICES = (('sleeping', 'Sleeping'),
              ('jumping', 'jumping'),
        )



class SpendingModel(models.Model):
     my_field = MultiSelectField(choices= CHOICES, default='False')

