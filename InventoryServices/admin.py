from django.contrib import admin
from .models import Warehouse
# Register your models here.
@admin.register(Warehouse)
class Warehouse(admin.ModelAdmin):
    list_display = ("id", "name", "city", "state", "country", "status", "size", "capacity", "warehouse_type", "created_at","warehouse_manager")
    list_filter = ("status", "size", "capacity", "warehouse_type", "city", "state", "country")
    search_fields = ("name", "city", "state", "country", "pincode", "warehouse_manager__username", "email", "phone")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
