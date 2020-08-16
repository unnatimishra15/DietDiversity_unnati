from django.shortcuts import render

# Create your views here.

from .form import LoginForm
from .models import LoginModel


# Create your views here.

def Login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form' : form
    }
    return render(request,'Login.html',context)


