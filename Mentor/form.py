from django import forms

from .models import MentorFormModel


class MentorForm(forms.ModelForm):
       
    class Meta: 
        model = MentorFormModel
        fields = [
            
            'MentorType',
            'Institute',
            'StudentRegistered',
        ]