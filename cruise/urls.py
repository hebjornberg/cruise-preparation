from django.urls import path, include 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_cruise/', views.create_cruise, name='create_cruise'),
    path('cruise_list/', views.cruise_list, name='cruise_list'),
    path('cruise/<int:cruise_id>/', views.cruise_detail, name='cruise_detail'),
    path('<int:cruise_id>/add_item/', views.add_item, name='add_item'),
    path('cruise/<int:cruise_id>/edit/', views.create_cruise, name='edit_cruise'),
    path('cruise/<int:cruise_id>/item/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('register/', views.registration_form, name='registration_form'),
]