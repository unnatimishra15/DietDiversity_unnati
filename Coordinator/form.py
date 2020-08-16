from django import forms

from .models import CoordinatorModel


class CoordinatorForm(forms.ModelForm):
       
    class Meta:
        model = CoordinatorModel
        fields = [
            'CoordinatorId',
            'CoordinatorName',
            'Institute'
           
        ]