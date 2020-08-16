# Generated by Django 3.0.8 on 2020-08-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerationformmodel',
            name='SpendingDay',
            field=models.CharField(choices=[('sleeping', 'Sleeping'), ('eating', 'Eating'), ('studying', 'Studying'), ('siting and working at a desk', 'Sitting and working at a desk'), ('sports training', 'Sports Training'), ('siting in front of the TV', 'Sitting in front of the TV'), ('sitind at the computer', 'Sitting at the computer'), ('playing outside', 'Playing outside'), ('running', 'Running'), ('zumba', 'Zumba'), ('aerobics', 'Aerobics'), ('briskwalking', ' Brisk walking'), ('yoga', 'Yoga'), ('meditation', 'Meditation')], default='Sleeping', max_length=100),
        ),
        migrations.AlterField(
            model_name='registerationformmodel',
            name='StudentClass',
            field=models.CharField(default='0', max_length=100),
        ),
    ]