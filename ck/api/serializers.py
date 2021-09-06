from rest_framework import serializers
from tweet.models import Tweet, Response as ResponseModel


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
