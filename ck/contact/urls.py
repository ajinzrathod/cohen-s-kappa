from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactHome, name='Contact Home Page'),
    path('success/', views.contactFormSuccess,
         name='Contact Form Success Page'),

]
