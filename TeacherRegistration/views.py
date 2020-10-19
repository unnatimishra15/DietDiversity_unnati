from django.shortcuts import render,redirect
#from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from .form import TeacherRegistrationForm
from .models import TeacherRegistrationModel
from .form import TeacherLoginForm
from .models import TeacherLoginModel


def teacherRegistration(request):
    form = TeacherRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form' : form
    }
    return render(request,'teacherregister.html',context)


def teacherLogin(request):
    form  = TeacherLoginForm(request.POST or None)
    u  = request.POST.get('UserName')
    p = request.POST.get('Password')
    if form.is_valid():
        # if TeacherRegistrationModel.objects.get(Email = 'u'):
        #     print("DOne")
        user = TeacherRegistrationModel.objects.get(Email = u)
        passwrd= TeacherRegistrationModel.objects.get(Password=p)
        print(user.Email)
        print(passwrd)
        if(user.Email==u and passwrd.Password==p):
            return render(request, 'HomePage.html')
        else:
            messages.error(request,'username or password not correct')
            return redirect('/teacherlogin/')

    else :
        form = TeacherLoginForm()
        return render(request, 'teacherlogin.html', {'form': form})
            



    