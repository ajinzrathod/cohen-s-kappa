from django.contrib import admin
from .models import Contact
# Register your models here.


# class ContactAdmin(admin.ModelAdmin):

    # list_display = ['user_id', 'issue', 'issue_image']


admin.site.register(Contact )  
# , ContactAdmin)
