from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import  DietRecallAppForm
from .models import DietRecallAppModel
# Create your views here.

class DietRecallAppView(TemplateView):
    template = 'dietrecall.html'


def dietRecallApp(request):
   
    form = DietRecallAppForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        
        'form' : form,
        'test': 'test'
    }


    return render(request,'dietrecall.html',context)

