# Generated by Django 3.2.6 on 2021-09-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_contact_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='issue',
            field=models.CharField(db_index=True, max_length=500),
        ),
    ]
