from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_cruise', views.create_cruise, name='create_cruise'),
    path('cruise_list', views.cruise_list, name='cruise_list'),
    path('<int:cruise_id>/', views.cruise_detail, name='cruise_detail'),
    path('<int:cruise_id>/add_item/', views.add_item, name='add_item')
]