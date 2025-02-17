from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'display_order', 'parent_id', 'domain_user_id', 'added_by_user_id', 'created_at', 'updated_at')


