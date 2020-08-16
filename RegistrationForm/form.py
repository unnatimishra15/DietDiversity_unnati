from django import forms

from .models import RegisterationFormModel


class RegistrationForm(forms.ModelForm):
       
    class Meta: 
        model = RegisterationFormModel
        fields = [
            'Name',
            'Age',
            'Gender',
            'StudentClass',
            'SpendingDay',
            'Height',
            'Weight',
            'Waist' ,     
            'Hip',
        ]