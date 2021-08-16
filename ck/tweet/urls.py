from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweetsHome, name='Tweets Home Page'),
]
