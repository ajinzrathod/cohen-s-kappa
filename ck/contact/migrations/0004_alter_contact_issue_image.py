# Generated by Django 3.2.6 on 2021-09-14 10:44

import contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_rename_issue_date_contact_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='issue_image',
            field=models.ImageField(upload_to='images/', validators=[contact.models.validate_image]),
        ),
    ]
