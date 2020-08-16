from django.db import models


from wagtail.core.models import Page
# Create your models here.

class CoordinatorPageModel(Page):

    template = "Coordinator.html"

ins = [
    ('school','School'),
    ('ngo','NGO'),
    
]

class CoordinatorModel(models.Model):
        CoordinatorId = models.CharField(max_length=100)
        CoordinatorName = models.CharField(max_length=100)
        Institute =  models.CharField(max_length=100,choices=ins,default=False)
