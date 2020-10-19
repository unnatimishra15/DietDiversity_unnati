from django.shortcuts import render,redirect
from .form import RegistrationForm
from .models import  RegisterationFormModel
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def register(request):
   
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            messages.add_message(request,messages.INFO,'Saved Successfully')
            return redirect(reverse('Display:display'))
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})