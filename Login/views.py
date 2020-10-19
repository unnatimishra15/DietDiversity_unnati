from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .form import LoginForm
from .models import LoginModel
from django.http import HttpResponseRedirect
# Create your views here.



# Create your views here.

def Login(request):
    # form = LoginForm(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context= {
    #     'form' : form
    # }
    # return render(request,'Login.html',context)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print('hii')
        print(username)
        if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to index page.
                    # messages.info(request,"login sucessfully")
                    return render(request,"sample.html")
                else:
                    # Return a 'disabled account' error message
                    messages.info(request,"You're account is disabled")
                    return HttpResponseRedirect("You're account is disabled.")
        else:
                # Return an 'invalid login' error message.
                print ("invalid login details " + username + " " + password)
                messages.info(request,"Invalid login details"+ username + " " + password)
                return render(request,'Login.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'Login.html')


def MultipleForms(request):


    return render(request,'sample.html')

