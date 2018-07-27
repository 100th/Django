from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Item, Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'name', 'amount']

    def photo_tag(self, item):
        if item.photo:
            return mark_safe('<img src="{}" style="width: 75px;" />'.format(item.photo.url))
        return None


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['imp_uid', 'user', 'name', 'amount_html', 'status_html', 'paid_at', 'receipt_link']
