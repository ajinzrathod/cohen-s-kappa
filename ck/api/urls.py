from django.urls import path
from . import views


urlpatterns = [
    path('get-all-tweets/', views.getAllTweets, name='Get all Tweets'),
    path('get-tweet/<int:id>/', views.getTweet, name='Get Tweet'),

    path('mark-response/<int:tweet_id>/<str:tweet_response>/',
         views.markResponse, name='Mark Response'),
    path('mark-priority/<int:tweet_id>/<int:priority>/',
         views.markPriority, name='Mark Priority'),

    path('get-next-tweet/',
         views.getNextTweet, name='Get Next Tweet'),

    path('compare/<str:user1>/<str:user2>/',
         views.calculateKappa, name='Compare using Kappa'),

    path('search-user/<str:searchText>/',
         views.searchUser, name='Search User'),
]
