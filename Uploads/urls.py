from django.urls import path
from . import views

urlpatterns = [
        path('upload/',views.upload_articles,name = "uploadarticles"),
        path('list/',views.articles_list,name = "articlelist")
]