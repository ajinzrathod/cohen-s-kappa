# Generated by Django 3.2.6 on 2021-08-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='common_for_all',
            field=models.BooleanField(default=False),
        ),
    ]
