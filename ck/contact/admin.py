from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'issue', 'date_created']


admin.site.register(Contact, ContactAdmin)
