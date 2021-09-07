# from django.shortcuts import render
from tweet.models import (
    Tweet, Response as ResponseModel,
    VALID_RESPONSES, POSITIVE,
    VALID_PRIORITIES, NO_PRIORITY)
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User
from django.db.models import F

# Rest Framework
from .serializers import TweetSerializer, ResponseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# https://www.youtube.com/watch?v=TmsD8QExZ84&t=1104s
# Create your views here.

@api_view(['GET', 'POST'])
def getAllTweets(request):
    """
    Source:
    https://docs.microsoft.com/en-us/dotnet/api/system.web.script.serialization.javascriptserializer.maxjsonlength?view=netframework-4.8
    The maximum length of JSON strings. The default is 2097152 characters,
    # which is equivalent to 4 MB of Unicode string data.
    """

    # Thus each tweet has maximum of 280 Chars and its "id" have 19 digits max
    # "9,223,372,036,854,775,808"

    # 280 + 19 = 299. Rounding off to 300 characters
    # 2097152 / 300 = 6990.506666667
    # but for safe side we will load only 5000 tweets. If more than that,
    # download option will be there

    all_tweets = Tweet.objects.all()
    if all_tweets.count() > 5000:
        content = {'Too many tweets': 'Tweets are greater than 5000. '
                   'Consider downloading the file instead'}

        # HTTP Status 204 (No Content) indicates that the server has
        # successfully fulfilled the request and that there is no content to
        # send in the response payload body. The server might want to return
        # updated meta-information in the form of entity-headers, which, if
        # present, SHOULD be applied to the current document’s active view if
        # any.
        return Response(content, status=204)
    serializer = TweetSerializer(all_tweets, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getTweet(request, id):
    try:
        tweet = Tweet.objects.get(id=id)
    except ObjectDoesNotExist:
        content = {}
        return Response(content, status=400)

    serializer = TweetSerializer(tweet, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def markResponse(request, tweet_id, tweet_response):
    # converting tweet_response from str to int to accept negative values also
    try:
        tweet_response = int(tweet_response)
    except ValueError:
        print("'tweet_response' must be convertible to an integer.")
        content = {
            'description': 'tweet_response must be convertible to an integer',
            'message': 'Failed'
        }
        return Response(content, status=400)

    # checking if user has logged in
    if not request.user.is_authenticated:
        content = {
            'description': 'Authentication Failed',
            'message': 'Failed'
        }
        return Response(content, status=403)

    # Checking if Tweet Exists
    try:
        Tweet.objects.get(id=tweet_id)
    except ObjectDoesNotExist:
        content = {
            'description': 'No such Tweet Exists',
            'message': 'Failed'
        }
        return Response(content, status=403)

    if tweet_response not in VALID_RESPONSES:
        content = {
            'description': 'Not a VALID REPONSE',
            'message': 'Failed'
        }
        return Response(content, status=400)

    # Saving Data
    try:
        obj, created = ResponseModel.objects.update_or_create(
            user_id=request.user,
            tweet_id=Tweet.objects.get(pk=tweet_id),
            defaults={
                'response': tweet_response,
            },
        )
    except Exception as e:
        print(e)
        content = {
            'description': 'Error occured while saving data',
            'message': 'Failed'
        }
        return Response(content, status=403)

    # Getting saved data
    try:
        result = ResponseModel.objects.get(
            user_id=request.user,
            tweet_id=tweet_id,
        )
    except ObjectDoesNotExist:
        content = {}
        return Response(content, status=400)

    serializer = ResponseSerializer(result, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def markPriority(request, tweet_id, priority):
    # checking if user has logged in
    if not request.user.is_authenticated:
        content = {
            'description': 'Authentication Failed',
            'message': 'Failed'
        }
        return Response(content, status=403)

    # Checking if Tweet Exists
    try:
        Tweet.objects.get(id=tweet_id)
    except ObjectDoesNotExist:
        content = {
            'description': 'No such Tweet Exists',
            'message': 'Failed'
        }
        return Response(content, status=403)

    if priority not in VALID_PRIORITIES:
        content = {
            'description': 'Not a VALID PRIORITY',
            'message': 'Failed'
        }
        return Response(content, status=400)

    # priority will only be changed if response is postive,
    # coz pre_save method is used
    try:
        # Saving Data
        obj, created = ResponseModel.objects.update_or_create(
            user_id=request.user,
            tweet_id=Tweet.objects.get(pk=tweet_id),
            defaults={
                'priority': priority,
            },
        )
    except Exception as e:
        print(e)
        content = {
            'description': 'Error occured while saving data',
            'message': 'Failed'
        }
        return Response(content, status=403)

    # Getting saved data
    try:
        result = ResponseModel.objects.get(
            user_id=request.user,
            tweet_id=tweet_id,
        )
    except ObjectDoesNotExist:
        content = {}
        return Response(content, status=400)

    serializer = ResponseSerializer(result, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getNextTweet(request):
    # checking if user has logged in
    if not request.user.is_authenticated:
        content = {
            'description': 'Authentication Failed',
            'message': 'Failed'
        }
        return Response(content, status=403)

    try:
        q1 = ResponseModel.objects.filter(user_id=request.user.id)
        q2 = Tweet.objects.exclude(
            id__in=q1.values_list('tweet_id', flat=True))
        q3 = q2.order_by('-common_for_all', 'id')[:1]

    except ObjectDoesNotExist:
        content = {}
        return Response(content, status=400)

    serializer = TweetSerializer(q3, many=True)
    return Response(serializer.data)
