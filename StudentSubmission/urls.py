from django.urls import path
from . import views

urlpatterns = [
        path('',views.studentsubmission,name = "login")
]