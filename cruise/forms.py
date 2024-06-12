from django import forms 
from .models import Cruise, Item

class CruiseForm(forms.ModelForm): 
    class Meta: 
        model = Cruise
        fields = ['cruise_number', 'start_date', 'end_date']

class ItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ['name', 'quantity', 'description', 'cruise']