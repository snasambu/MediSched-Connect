from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'date_of_birth', 'contact_info', 'gender', 'specialization', 'availability')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
