# Generated by Django 3.0.8 on 2020-08-01 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterationFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField(default=0)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=20)),
                ('StudentClass', models.CharField(default='none', max_length=100)),
                ('SpendingDay', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Sleeping', max_length=100)),
                ('Height', models.IntegerField(default=0)),
                ('Weight', models.IntegerField(default=0)),
                ('Waist', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]