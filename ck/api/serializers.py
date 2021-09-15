from rest_framework import serializers
from tweet.models import Tweet, Response as ResponseModel
from django.contrib.auth.models import User


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        # fields = ['tweet']


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'
        # fields = ['tweet']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
