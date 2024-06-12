from django import forms 
from .models import Cruise

class CruiseForm(forms.ModelForm): 
    class Meta: 
        model = Cruise
        fields = ['cruise_number', 'start_date', 'end_date']