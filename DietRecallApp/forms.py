from django import forms
from .models import DietRecallAppModel
from datetimepicker.widgets import DateTimePicker

class DietRecallAppForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = DietRecallAppModel
        fields = ('Meal','Description','EatDate','EatTime')
        