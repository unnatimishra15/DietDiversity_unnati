from django.urls import path
from . import views

urlpatterns = [
        path('student/',views.studentsubmission,name = "login")
]