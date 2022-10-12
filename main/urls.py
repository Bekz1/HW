
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.base, name='home'),

    path('cars/', views.cars, name='cars'),
    path('cars/add/', views.add_cars, name='add_cars'),
    path('cars/view/<int:pk>/', views.view_cars, name='view_cars'),
    path('cars/edit/<int:pk>/', views.edit_cars, name='edit_cars'),
    path('cars/delete/<int:pk>/', views.delete_cars, name='delete_cars'),

    path('drivers/', views.drivers, name='drivers'),
    path('/drivers/add/', views.add_drivers, name='add_drivers'),
    path('/drivers/edit/<int:pk>/', views.edit_drivers, name='edit_drivers'),
    path('/drivers/delete/<int:pk>/', views.delete_drivers, name='delete_drivers'),
   


    
]