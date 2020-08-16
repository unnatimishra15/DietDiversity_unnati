from django.shortcuts import render

# Create your views here.

from .form import MentorForm
from .models import MentorFormModel


# Create your views here.

def mentor(request):
    form = MentorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form' : form
    }
    return render(request,'mentor.html',context)

