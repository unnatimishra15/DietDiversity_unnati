from django.shortcuts import render
from .form import ImageForm
# Create your views here.


def studentsubmission(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            img_url =img_obj.image.url
            return render(request, 'studentsubmission.html', {'form': form, 'img_obj': img_obj,'img_url': img_url})
    else:
        form = ImageForm()
    return render(request, 'studentsubmission.html', {'form': form})
