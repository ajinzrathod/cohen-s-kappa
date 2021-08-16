from django.urls import path
from . import views


urlpatterns = [
    path('get-all-tweets/', views.getAllTweets, name='Get all Tweets'),
    path('get-tweet/<int:id>/', views.getTweet, name='Get Tweet'),
]
