from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactHome, name='Contact Home Page'),
]
