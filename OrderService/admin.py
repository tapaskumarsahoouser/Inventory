from django.contrib import admin
from OrderService.models import * # Adjust the import based on your app name

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'po_code', 'supplier_id', 'warehouse_id', 'po_date', 'status')
    search_fields = ('po_code', 'supplier_id__username')
    list_filter = ('status', 'payment_status', 'po_date')
    ordering = ('-po_date',)


# @admin.register(PurchaseOrder)
# class PurchaseOrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'po_code', 'supplier_id', 'po_date', 'status', 'created_at')
#     list_filter = ('status', 'payment_status', 'po_date', 'created_at')
#     search_fields = ('po_code', 'supplier_id__username', 'supplier_id__email')
#     ordering = ('-created_at',)

@admin.register(PurchaseOrderItems)
class PurchaseOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'po_id', 'product_id', 'quantity_ordered', 'buying_price', 'selling_price', 'amount_ordered')
    list_filter = ('po_id', 'product_id')
    search_fields = ('po_id__po_code', 'product_id__name')
    ordering = ('-created_at',)
