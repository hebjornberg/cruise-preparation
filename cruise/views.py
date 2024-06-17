from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Cruise, Item
from .forms import CruiseForm, ItemForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registration_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required
def create_cruise(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST)
        if form.is_valid():
            cruise = form.save(commit=False)
            cruise.creator = request.user
            cruise.save()
            return redirect('cruise_detail', cruise_id=cruise.id)
    else: 
        form = CruiseForm()
    return render(request, 'cruise/create_cruise.html', {'form': form})

def cruise_detail(request, cruise_id):
    cruise = get_object_or_404(Cruise, id=cruise_id)
    items = cruise.items.all()
    return render(request, 'cruise/cruise_detail.html', {'cruise': cruise, 'items': items})

@login_required
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

def cruise_list(request):
    cruises = Cruise.objects.all()
    return render(request, 'cruise/cruise_list.html', {'cruises': cruises})
