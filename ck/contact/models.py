from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Contact(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    issue = models.CharField(max_length=280, db_index=True)
    issue_image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contact Us')
