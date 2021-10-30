from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','solution','category']
        widgets = {
            'name':forms.Textarea(attrs={'id':'problem-field', 'class':'resize-field','placeholder':'What are we doing wrong? Write in 100 characters.'}),
            'solution':forms.Textarea(attrs={'id':'solution-field', 'class':'resize-field','placeholder':'What solution do you propose?'}),
            }