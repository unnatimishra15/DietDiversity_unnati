from django.shortcuts import render,redirect
from .form import RegistrationForm
from .models import  RegisterationFormModel


# Create your views here.
def register(request):
   
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form' : form,
        'test': 'test'
    }

    return render(request,'register.html',context)
        

    