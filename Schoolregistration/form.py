from django import forms

from .models import SchoolModel


class SchoolRegistrationForm(forms.ModelForm):
       
    class Meta: 
        model = SchoolModel
        fields = [
            
            'SchoolID',
            'SchoolName',
            'CoordinatorId',
        ]