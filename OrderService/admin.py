from django.contrib import admin
from OrderService.models import PurchaseOrder  # Adjust the import based on your app name

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'po_code', 'supplier_id', 'warehouse_id', 'po_date', 'status')
    search_fields = ('po_code', 'supplier_id__username')
    list_filter = ('status', 'payment_status', 'po_date')
    ordering = ('-po_date',)
