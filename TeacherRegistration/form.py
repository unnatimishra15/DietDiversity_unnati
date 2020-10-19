from django import forms

from .models import TeacherRegistrationModel
from .models import TeacherLoginModel

class TeacherRegistrationForm(forms.ModelForm):
       
    class Meta: 
        model = TeacherRegistrationModel
        fields = [
            'Name',
            'Institute',
            'Gender',
            'Email' ,     
            'ContactNumber',
            'Password',
        ]
        widgets = {
             'Password': forms.PasswordInput()
         }

class TeacherLoginForm(forms.ModelForm):
    class Meta:
        model = TeacherLoginModel
        fields = [
            'UserName',
            'Password',

    ]
        widgets = {
             'Password': forms.PasswordInput()
         }
