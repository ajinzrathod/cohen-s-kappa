# from django.shortcuts import render
from tweet.models import Tweet
from django.core.exceptions import ObjectDoesNotExist

# Rest Framework
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
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


@api_view(['GET'])
def getTweet(request, id):
    # 400 Bad Request

    # The HyperText Transfer Protocol (HTTP) 400 Bad Request response status
    # code indicates that the server cannot or will not process the request due
    # to something that is perceived to be a client error (e.g., malformed
    # request syntax, invalid request message framing, or deceptive request
    # routing).
    try:
        tweet = Tweet.objects.get(id=id)
    except ObjectDoesNotExist:
        content = {}
        return Response(content, status=400)

    serializer = TweetSerializer(tweet, many=False)
    return Response(serializer.data)

# https://www.youtube.com/watch?v=TmsD8QExZ84&t=1104s
