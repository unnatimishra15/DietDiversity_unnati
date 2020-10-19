from django.urls import path
from . import views

urlpatterns = [
        path('',views.BulkStudentRegistrationView,name = "bulkRegistration")
]