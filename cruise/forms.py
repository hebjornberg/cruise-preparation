from django import forms 
from .models import Cruise, Item

class CruiseForm(forms.ModelForm): 
    class Meta: 
        model = Cruise
        fields = ['cruise_number', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'placeholder': 'Format: YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'Format: YYYY-MM-DD'}),
        }

class ItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ['name', 'quantity', 'description']