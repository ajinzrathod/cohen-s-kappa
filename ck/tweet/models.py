from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


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
VALID_PRIORITIES = (NO_PRIORITY, LOW, MODERATE, HIGH, EXTREME)

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
    priority = models.SmallIntegerField(
        choices=PRIORITES, default=NO_PRIORITY,
        help_text=_('Priority will auto set to \"No Priority\"'
                    ' if Response is NOT postive.<br/>'
                    'Priority will auto set to \"Moderate\"'
                    ' if Response is postive and Priority is \"No Priority\".')
    )

    class Meta:
        verbose_name = _('Response')
        verbose_name_plural = _('Responses')


@receiver(pre_save, sender=Response)
def response_pre_save(sender, instance, *args, **kwargs):
    """
    If you dont include the sender argument in the decorator, like
    @receiver(pre_save, sender=MyModel), the callback will be called for all
    models.
    """
    if instance.response != POSITIVE:
        instance.priority = NO_PRIORITY

    if instance.response == POSITIVE and instance.priority == NO_PRIORITY:
        instance.priority = MODERATE

    """
    in post save, .save() "might" be called. I am not sure, read this warning:
    https://docs.djangoproject.com/en/3.2/ref/signals/#module-django.db.models.signals

    or save() should be called only if save() method is overriden. Not sure
    """
