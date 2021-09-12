from django.urls import path
from . import views


urlpatterns = [
    path('', views.compareHome, name='Compare Home Page'),
]
