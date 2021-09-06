from django.contrib import admin
from .models import Tweet, Response
from django.db import models
from django.forms import Textarea
from django.utils.translation import ngettext
from django.contrib import messages


# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    list_filter = ['common_for_all']
    search_fields = ['id', 'tweet']
    list_display = ['id', 'tweet', 'common_for_all']

    formfield_overrides = {
        models.CharField: {
            'widget': Textarea(attrs={
                'rows': 10, 'cols': 80
            })
        },
    }

    actions = [
        'mark_as_common',
        'unmark_from_common'
    ]

    def mark_as_common(self, request, queryset):
        updated = queryset.update(common_for_all=True)
        self.message_user(request, ngettext(
            '%d tweet was successfully marked as Common.',
            '%d tweets were successfully marked as Common.',
            updated,
        ) % updated, messages.SUCCESS)

    def unmark_from_common(self, request, queryset):
        updated = queryset.update(common_for_all=False)
        self.message_user(request, ngettext(
            '%d tweet was successfully marked as NOT Common.',
            '%d tweets were successfully marked as NOT Common.',
            updated,
        ) % updated, messages.SUCCESS)

    mark_as_common.short_description = "Mark as Common for All"
    unmark_from_common.short_description = "Remove from Common for All"


class ResponseAdmin(admin.ModelAdmin):
    list_filter = ['response']
    search_fields = ['user_id', 'tweet_id', 'response']
    list_display = ['id', 'user_id', 'tweet_id', 'response']

    # dont forget comma at end if using only 1 item in below tuple
    # raw_id_fields = ("user_id", "tweet_id")
    raw_id_fields = ("tweet_id", )


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Response, ResponseAdmin)
