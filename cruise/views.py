from django.shortcuts import render
from django.http import HttpResponse
from .models import Cruise
from .forms import CruiseForm, ItemForm

# Create your views here.
def create_cruise(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = CruiseForm()
    return render(request, 'create_cruise.html', {'form': form})

def add_item(request, cruise_id):
    cruise = get_object_or_404(Cruise, id=cruise_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.cruise = cruise
            item.save()
#           return
    else: 
        form = ItemForm()
    return render(request, 'cruise/add_item.html', {'cruise': cruise})