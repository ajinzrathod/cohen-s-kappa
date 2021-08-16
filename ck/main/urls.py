from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home Page'),
    path('login/', views.home, name='Login Page'),
    path('logout/', views.logout, name='Logout Page'),
    path('404/', views.error_404, name='Error 404 - Page not found'),
    path('403/', views.error_403, name='Error 403 - Permission Denied'),
    path('500/', views.error_500, name='Error 500 - Internal Server Error'),
    path('tos/', views.tos, name='Terms of Service'),
    path('privacy-policy/', views.privacy_policy, name='Privacy Policy'),
]
