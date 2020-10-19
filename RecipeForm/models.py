from django.db import models

from wagtail.core.models import Page
# Create your models here.
process = [
    ('sf','Shallow Fried'),
    ('df','Deep Fried'),
    ('bo','Boiled'),
    ('ba','Baked'),
    ('st','Steamed'),
    ('rs','Roasted'),
    ('ca','Canned'),
    ('bm','Bought From Market')
]

recipetype= [

            ('maincourse','Main Course'),
            ('snacks','Snacks'),

]

class RecipeModel(Page):

    template = "RecipeForm.html"
    


class Recipe(models.Model):
        RecipeName = models.CharField(max_length=100)
        DishType = models.CharField(choices=recipetype,max_length=100,default='Snacks')
        CookingProcess = models.CharField(choices=process,max_length=100,default='Shallow Fried')
        ExplainDish= models.CharField(max_length=500)
        objects = models.Manager()
 