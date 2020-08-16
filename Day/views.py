from django.shortcuts import render
from .form import DaySpendForm
from .models import SpendingModel


# Create your views here.

def dayspend(request):
    if request.method == 'POST':
     form = DaySpendForm(request.POST or None)
     if form.is_valid():
        form.save()

        context= {
        'form' : form,
        'test': 'test'
         }


    return render(request,'dayspending.html',context)

