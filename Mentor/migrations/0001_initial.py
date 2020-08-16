# Generated by Django 3.0.8 on 2020-08-01 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MentorType', models.CharField(choices=[('mother', 'Mother'), ('teacher', 'Teacher'), ('socialworker', 'Social Worker'), ('teamleader', 'Team Leader'), ('studentmentor', 'Student Mentor')], default='studentmentor', max_length=20)),
                ('Institute', models.CharField(choices=[('school', 'School'), ('ngo', 'NGO')], default='school', max_length=20)),
                ('StudentRegistered', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MentorFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]