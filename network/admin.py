from django.contrib import admin
from .models import NetworkNode, Product
from django.utils.html import format_html

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'city', 'country', 'supplier_link', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    list_select_related = ('supplier',)

    def supplier_link(self, obj):
        """Ссылка на поставщика"""
        if obj.supplier:
            return format_html(
                '<a href="/admin/network/networknode/{}/change/">{}</a>',
                obj.supplier.id,
                obj.supplier.name
            )
        return "Нет поставщика"

    supplier_link.short_description = 'Поставщик'

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    actions = [clear_debt]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
    list_filter = ('release_date',)
    search_fields = ('name', 'model')
