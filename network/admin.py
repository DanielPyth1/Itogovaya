from django.contrib import admin
from .models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'city', 'country', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    list_select_related = ('supplier',)

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    actions = [clear_debt]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
    list_filter = ('release_date',)
    search_fields = ('name', 'model')
