from django import forms
from .models import Articles

class ArticleForm(forms.Form):
    class Meta:
        model = Articles,
        fields = ('name','title','uploadfile')
