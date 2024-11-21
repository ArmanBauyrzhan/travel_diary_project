
from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list, name='travel_list'),
    path('create/', views.create_travel, name='create_travel'),
]
