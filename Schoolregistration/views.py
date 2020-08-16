from django.shortcuts import render

# Create your views here.

from .form import SchoolRegistrationForm
from .models import SchoolModel


# Create your views here.

def school(request):
    form = SchoolRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context= {
        'form' : form
    }
    return render(request,'school.html',context)


def displaySchoolDetails(request):
    obj = SchoolModel.objects.all()
    context = {
            'SchoolName':obj.SchoolName,
            'test':'test',
    }
      
    return render(request,'schooldisplay.html',context)