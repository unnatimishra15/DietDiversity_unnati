from django import forms

from .models import SpendingModel


class DaySpendForm(forms.ModelForm):
       
    class Meta:
        model = SpendingModel
        fields = [
            'my_field'
           
           
        ]