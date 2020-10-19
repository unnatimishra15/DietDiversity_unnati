from django.db import models

# Create your models here.
gender = [
    ('male', 'Male'),
    ('female', 'Female'),
 ]
TeacherInstitute = [
     ('School', 'School'),
     ('NGO', 'NGO'),

]

class TeacherRegistrationModel(models.Model):
    Name = models.CharField(max_length=50)
    Institute = models.CharField(choices=TeacherInstitute, default="School", max_length=10)
    Gender = models.CharField(choices=gender,default="Male",max_length=10)
    Email =  models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    ContactNumber= models.CharField(max_length=10)
    objects = models.Manager()


class TeacherLoginModel(models.Model):
    UserName =  models.EmailField(max_length=100)
    Password  = models.CharField(max_length=100)
    objects = models.Manager()