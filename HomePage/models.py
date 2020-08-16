from django.db import models
from wagtail.core.models import Page
# Create your models here.



class HomePageModel(Page):

    template = "HomePage.html"
    