from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'product', 'quantity', 'created_at')
    list_filter = ('user', 'product')

    def get_username(self, obj):
        return obj.user.username if obj.user else 'کاربر ناشناس'
    get_username.short_description = 'کاربر'