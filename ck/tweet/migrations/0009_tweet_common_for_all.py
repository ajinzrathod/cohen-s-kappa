# Generated by Django 4.0 on 2021-12-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0008_remove_tweet_common_for_all'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='common_for_all',
            field=models.BooleanField(default=False),
        ),
    ]