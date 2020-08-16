from django.db import models
from wagtail.core.models import Page
# Create your models here.

mentortype = [
    ('mother', 'Mother'),
    ('teacher', 'Teacher'),
    ('socialworker', 'Social Worker'),
    ('teamleader', 'Team Leader'),
    ('studentmentor', 'Student Mentor'),
 ]

institute = [
      ('school','School'),
      ('ngo','NGO'),
      

  ]

class MentorFormPage(Page):

    template = "mentor.html"
    
class MentorFormModel(models.Model):
        MentorType= models.CharField(choices=mentortype, max_length= 20, default='studentmentor')
        Institute  = models.CharField(choices= institute, max_length= 20, default='school')
        StudentRegistered  = models.CharField(max_length= 50)
        