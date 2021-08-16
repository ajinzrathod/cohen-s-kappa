# Generated by Django 3.2.6 on 2021-08-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(db_index=True, max_length=280)),
            ],
            options={
                'verbose_name': 'Tweet',
                'verbose_name_plural': 'Tweets',
            },
        ),
    ]
