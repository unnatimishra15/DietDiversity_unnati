from django.urls import path
from . import views

urlpatterns = [
        path('form/',views.mentor,name = "mentorform")
]