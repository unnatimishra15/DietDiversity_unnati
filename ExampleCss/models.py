from django.db import models
from wagtail.core.models import Page
from django.shortcuts import render

# Create your models here.


class TestCss(Page):
    tempalate  = "TestCss.html"


def ExampleCss(request):

        
    return(request,"TestCss.html")
   
