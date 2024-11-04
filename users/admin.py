from django.contrib import admin
from .models import MailingUser


@admin.register(MailingUser)
class MailingUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'country')
    list_filter = list_display
    search_fields = ('username', 'email', 'phone_number', 'country')
    