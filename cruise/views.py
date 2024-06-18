from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
        #    user = authenticate(username=username, password=password)
        #    login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required
def create_cruise(request, cruise_id=None):
    cruise = None
    if cruise_id:
        cruise = get_object_or_404(Cruise, id=cruise_id)
        if request.user != cruise.creator:
            return HttpResponse("You are not authorized to update this cruise.")

    if request.method == 'POST':
        if cruise:
            form = CruiseForm(request.POST, instance=cruise)
        else:
            form = CruiseForm(request.POST)
        if form.is_valid():
            cruise = form.save(commit=False)
            cruise.creator = request.user
            cruise.save()
            return redirect(reverse('cruise_detail', args=[cruise.id]))
    else:
        if cruise:
            form = CruiseForm(instance=cruise)
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
            return redirect(reverse('cruise_detail', args=[cruise.id]))
    else:
        form = ItemForm()
    return render(request, 'cruise/add_item.html', {'cruise': cruise, 'form': form})

@login_required
def edit_item(request, cruise_id, item_id):
    cruise = get_object_or_404(Cruise, id=cruise_id)
    item = get_object_or_404(Item, id=item_id, cruise=cruise)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('cruise_detail', args=[cruise.id]))
    else:
        form = ItemForm(instance=item)

    return render(request, 'cruise/edit_item.html', {'form': form, 'cruise': cruise, 'item': item})

def cruise_list(request):
    cruises = Cruise.objects.all()
    return render(request, 'cruise/cruise_list.html', {'cruises': cruises})
