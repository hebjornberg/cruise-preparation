from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cruise(request): 
    return HttpResponse("Cruise preparation")
