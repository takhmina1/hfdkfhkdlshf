from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ()}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Codes'), {'fields': ('activation_code', 'reset_code')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'is_verified')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_verified')
    search_fields = ('email',)
    ordering = ('email',)
    # Ensure these attributes are not defined since 'groups' and 'user_permissions' do not exist
    filter_horizontal = ()
    filter_vertical = ()

admin.site.register(User, UserAdmin)
