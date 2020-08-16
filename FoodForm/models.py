from django.db import models
from wagtail.core.models import Page
# Create your models here.

class FoodPageModel(Page):

    template = "Food.html"

meal = [
    ('morning','Morning'),
    ('afternoon','Afternoon'),
    ('evening','Evening'),
    ('dinner','Dinner'),
    ('other','Any Other Time'),
   
]
taste = [
    ('sweet','Sweet'),
    ('sour','Sour'),
    ('salt','Salt'),
    ('hot','Hot'),
    ('mixed','Mixed'),

]
class FoodModel(models.Model):
        FoodId = models.CharField(max_length=100)
        FoodName = models.CharField(max_length=100)
        MealTime =  models.CharField(max_length=100,choices=meal,default=False)
        Taste  = models.CharField(max_length=100,choices=taste,default=False)
        MajorIngredient = models.CharField(max_length=200 )
        SpecialIngredient = models.CharField(max_length=500 )
