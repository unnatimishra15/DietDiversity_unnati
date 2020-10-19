from django.db import models

# Create your models here.
meals = [
    ('BreakFast', 'BreakFast'),
    ('Lunch', 'Lunch'),
    ('Evening Snacks',' Evening Snacks'),
    ('Dinner','Dinner')

]
# Create your models here.
class DietRecallAppModel(models.Model):
    Meal = models.CharField(choices=meals,max_length=50,default="Breakfast")
    Description = models.CharField(max_length=200)
    EatDate = models.DateField()
    EatTime = models.DateTimeField()
    