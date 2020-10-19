from django.shortcuts import render
from django.views.generic import TemplateView
from RegistrationForm.form import RegistrationForm
from RegistrationForm.models import RegisterationFormModel
from django.core import serializers
# Create your views here.

class DisplayView(TemplateView):
    template = 'display.html'

def display(request):
    labels = []
    hip = []
    form = RegistrationForm()
    data = RegisterationFormModel.objects.all()
    serialdata= serializers.serialize("json",data)
  
    for obj in serializers.deserialize("json", serialdata):
        labels.append(obj.object.Name)
        hip.append(obj.object.Hip)
        '''print(labels)'''

    '''for h in data:
        labels.append(h.Name)
        hip.append(h.Hip)
    print(type(labels))
    print(type(hip))'''
    args= {'form' : form,'test':'test','labels': labels,'hip': hip,'data':data,'obj':obj}
    return render(request,'display.html',args)




   