from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'name', 'amount']

    def photo_tag(self, item):
        if item.photo:
            return mark_safe('<img src="{}" style="width: 75px;" />'.format(item.photo.url))
        return None
