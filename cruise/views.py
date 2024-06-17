from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cruise, Item
from .forms import CruiseForm, ItemForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_cruise(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST)
        if form.is_valid():
            cruise = form.save()
            return redirect('cruise_detail', cruise_id=cruise.id)
    else: 
        form = CruiseForm()
    return render(request, 'cruise/create_cruise.html', {'form': form})

def cruise_detail(request, cruise_id):
    cruise = get_object_or_404(Cruise, id=cruise_id)
    items = cruise.items.all()
    return render(request, 'cruise/cruise_detail.html', {'cruise': cruise, 'items': items})

def add_item(request, cruise_id):
    cruise = get_object_or_404(Cruise, id=cruise_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.cruise = cruise
            item.save()
            return redirect('cruise_detail', cruise_id=cruise.id)
    else: 
        form = ItemForm()
    return render(request, 'cruise/add_item.html', {'cruise': cruise, 'form': form})