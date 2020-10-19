from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
	        form.save()
		    #messages.success(request, 'Registered successfully')
	    return render(request,'Login.html')
    else:
	    form = UserCreationForm()

    return render(request, "registration.html",{"form":form})

def login(request):
	if request.method == "POST":
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			return redirect(request,'profile.html')

	

	else:

		form = AuthenticationForm() 

	return render(request,'Login.html',{"form":form})
