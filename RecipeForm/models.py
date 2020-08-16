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
        DishType = models.CharField(max_length=100 ,choices=recipetype,default=False)
        CookingProcess = models.CharField(max_length=100,choices=process,default=False)
        ExplainDish= models.CharField(max_length=500)
 