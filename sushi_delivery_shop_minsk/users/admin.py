from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telegram_id', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telegram_id', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
