from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Tweet(models.Model):
    # https://stackoverflow.com/a/7354680/11605100
    # https://stackoverflow.com/a/8698298/11605100
    tweet = models.CharField(max_length=280, db_index=True)

    class Meta:
        verbose_name = _('Tweet')
        verbose_name_plural = _('Tweets')


# class CSV(models.Model):
#     file = models.
