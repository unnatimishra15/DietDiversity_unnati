from django.contrib import admin
from .models import UserType
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(UserType)
