# Generated by Django 3.0.8 on 2020-09-25 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeForm', '0005_auto_20200925_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='CookingProcess',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='DishType',
        ),
    ]
