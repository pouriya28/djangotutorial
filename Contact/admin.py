from django.contrib import admin

# Register your models here.

from .models import Contactform

@admin.register(Contactform)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'time')
    search_fields = ('name', 'email')
    list_filter = ('time',)
