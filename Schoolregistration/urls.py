from django.urls import path
from . import views

urlpatterns = [
        path('registration/',views.school,name = "mentorform")
]