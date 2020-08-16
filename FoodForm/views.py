from django.shortcuts import render

from .form import FoodForm
from .models import FoodModel

# Create your views here.

def FoodPage(request):
    form1 = FoodForm(request.POST or None)
    if form1.is_valid():
        form1.save()

    context= {
        
        'form1' : form1,
        'test': 'test'
    }

    return render(request,'Food.html',context)

