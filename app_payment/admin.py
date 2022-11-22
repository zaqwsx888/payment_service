from django.contrib import admin
from .models import Item

admin.site.site_title = 'Админ-панель сервиса оплаты'
admin.site.site_header = 'Админ-панель сервиса оплаты'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name',)
