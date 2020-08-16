from django.shortcuts import render
from .form import CoordinatorForm
from .models import CoordinatorPageModel


# Create your views here.

def Coordinator(request):
    
    form = CoordinatorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form' : form,
        'test': 'test'
    }


    return render(request,'Coordinator.html',context)

