from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.core.exceptions import ValidationError
# Create your models here.


def validate_image(image):
    file_size = image.file.size
    LIMIT_KB = 300 * 1024
    if file_size > LIMIT_KB:
        raise ValidationError("Max size of file is %s KB" % LIMIT_KB)


class Contact(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    issue = models.CharField(
        max_length=500,
        db_index=True
    )
    issue_image = models.ImageField(
        upload_to='images/', validators=[validate_image])
    date_created = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contact Us')

    def save(self, *args, **kwargs):
        if self.user_id:
            self.user_id = request.user.id
        print(*args, **kwargs)
        super(Contact, self).save(*args, **kwargs)
