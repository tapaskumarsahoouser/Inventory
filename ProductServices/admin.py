from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'display_order', 'parent_id', 'domain_user_id', 'added_by_user_id', 'created_at', 'updated_at')


from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sku', 'brand', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'brand', 'category_id')
    search_fields = ('name', 'sku', 'brand', 'brand_model', 'category_id__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'image', 'description', 'html_description', 'highlights', 'specifications')
        }),
        ('Pricing & Stock', {
            'fields': ('sku', 'initial_buying_price', 'initial_selling_price', 'weight', 'dimensions', 'uom', 'color', 'tax_percentage')
        }),
        ('Brand & Category', {
            'fields': ('brand', 'brand_model', 'category_id', 'status')
        }),
        ('SEO Information', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        }),
        ('Additional Details', {
            'fields': ('addition_details',)
        }),
        ('Ownership & Timestamps', {
            'fields': ('domain_user_id', 'added_by_user_id', 'created_at', 'updated_at')
        }),
    )

    def get_queryset(self, request):
        """Optimize queries by selecting related fields."""
        return super().get_queryset(request).select_related('category_id', 'domain_user_id', 'added_by_user_id')

