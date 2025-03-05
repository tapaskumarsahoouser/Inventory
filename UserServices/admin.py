from django.contrib import admin
from .models import *

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'first_name', 'last_name', 'phone', 'dob', 'address', 'country', 'state', 'language', 'designation','role')

@admin.register(UserShippingAddress)
class UserShippingAddress(admin.ModelAdmin):
    list_display = ('id','user','address_type','address','city','state','pincode','country','created_at','updated_at')


@admin.register(Modules)
class Modules(admin.ModelAdmin):
    list_display = ('id','module_name','module_icon','is_menu','is_active','module_url','parent_id','display_order','module_description','created_at','updated_at')

@admin.register(ModuleUrls)
class ModuleUrls(admin.ModelAdmin):
    list_display = ('id','module','url','created_at','updated_at')

@admin.register(UserPermissions)
class UserPermissions(admin.ModelAdmin):
    list_display = ('id','user','module','is_permission','domain_user_id','updated_at')


@admin.register(Expoter)
class Expoter(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city', 'state', 'country', 'role', 'account_status', 'created_at')
    list_filter = ('country', 'role', 'account_status', 'plan_type', 'departMent')
    search_fields = ('email', 'phone', 'city', 'state', 'country', 'role')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Basic Information", {
            'fields': ('email', 'phone', 'address', 'city', 'state', 'pincode', 'country', 'profile_pic')
        }),
        ("Account Details", {
            'fields': ('account_status', 'role', 'dob', 'social_media_links', 'addition_details', 'language')
        }),
        ("Work Information", {
            'fields': ('departMent', 'designation', 'time_zone')
        }),
        ("Login Information", {
            'fields': ('last_login', 'last_device', 'last_ip')
        }),
        ("Financial Details", {
            'fields': ('currency', 'plan_type')
        }),
        ("Domain & User Management", {
            'fields': ('domain_user_id', 'domain_name', 'added_by_user_id')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def has_delete_permission(self, request, obj=None):
        """ Prevent deletion of users from the admin panel """
        return False  # Change to True if deletion is allowed

    def has_add_permission(self, request):
        """ Prevent addition of new users from the admin panel """
        return True  # Change to False if addition is not allowed