from django.urls import path
from . import views

urlpatterns = [
        path('',views.dietRecallApp,name = "dietrecall")
]