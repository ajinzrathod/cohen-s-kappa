from django.contrib import admin
from .models import Tweet
from django.db import models
from django.forms import Textarea


# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    search_fields = ['id', 'tweet']
    list_display = ['id', 'tweet']

    formfield_overrides = {
        models.CharField: {
            'widget': Textarea(attrs={
                'rows': 10, 'cols': 80
            })
        },
    }


admin.site.register(Tweet, TweetAdmin)
