from django.urls import path 
from . import views

urlpatterns = [
    path('', views.create_cruise, name='create_cruise'),
    path('<int:cruise_id>/add_item/', views.add_item, name='add_item')
]