from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class CameraView(TemplateView):
    template = 'CameraApp.html'


def camera(request):
    return render(request,'CameraApp.html')



