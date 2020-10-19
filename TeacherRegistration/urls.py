from django.urls import path
from . import views

urlpatterns = [
        path('register/',views.teacherRegistration,name = "TeacherRegistration"),
        path('login/',views.teacherLogin,name = "TeacherLogin")
]