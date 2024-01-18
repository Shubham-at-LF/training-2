from django.contrib import admin
from django.urls import path

from cpost import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('add/', views.add)
]