from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.


class Tweet(models.Model):
    # https://stackoverflow.com/a/7354680/11605100
    # https://stackoverflow.com/a/8698298/11605100
    tweet = models.CharField(max_length=280, db_index=True)
    common_for_all = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Tweet')
        verbose_name_plural = _('Tweets')


# class CSV(models.Model):
#     file = models.


NO_RESPONSE_OR_SKIP = 0
POSITIVE = 1
NEGATIVE = -1
NEVER_ASK_AGAIN = -2
VALID_RESPONSES = (NO_RESPONSE_OR_SKIP, POSITIVE, NEGATIVE, NEVER_ASK_AGAIN)

RESPONSES = (
    (NO_RESPONSE_OR_SKIP, 'No Response Or Skip'),
    (POSITIVE, 'Positive'),
    (NEGATIVE, 'Negative'),
    (NEVER_ASK_AGAIN, 'Never Ask Again'),
)

NO_PRIORITY = 0
LOW = 1
MODERATE = 2
HIGH = 3
EXTREME = 4

PRIORITES = (
    (NO_PRIORITY, 'No Priority'),
    (LOW, 'Low'),
    (MODERATE, 'Moderate'),
    (HIGH, 'High'),
    (EXTREME, 'Extreme'),
)


class Response(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    response = models.SmallIntegerField(choices=RESPONSES)
    priority = models.SmallIntegerField(choices=PRIORITES, default=NO_PRIORITY)

    class Meta:
        verbose_name = _('Response')
        verbose_name_plural = _('Responses')
