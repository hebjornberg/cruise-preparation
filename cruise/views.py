from django.shortcuts import render
from django.http import HttpResponse
from .models import Cruise
from .forms import CruiseForm

# Create your views here.
def create_cruise(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = CruiseForm()
    return render(request, 'create_cruise.html', {'form': form})