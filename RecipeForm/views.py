from django.shortcuts import render

from .form import RecipeForm
from .models import Recipe

# Create your views here.

def RecipePage(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form': form,
        'test': 'test',
    }

    return render(request,'RecipeForm.html',context)

