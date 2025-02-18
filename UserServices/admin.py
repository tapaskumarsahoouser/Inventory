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