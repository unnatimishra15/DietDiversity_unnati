# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RecipeformRecipemodel(models.Model):
    recipename = models.CharField(db_column='RecipeName', max_length=100)  # Field name made lowercase.
    dishtype = models.CharField(db_column='DishType', max_length=100)  # Field name made lowercase.
    cookingprocess = models.CharField(db_column='CookingProcess', max_length=100)  # Field name made lowercase.
    explaindish = models.CharField(db_column='ExplainDish', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecipeForm_recipemodel'
