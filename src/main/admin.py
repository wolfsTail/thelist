from django.contrib import admin

from main.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal Info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Permission',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            'Impotent dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )
