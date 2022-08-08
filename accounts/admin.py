from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'is_staff', 'is_active', 'is_teacher', 'science')
    list_filter = ('username', 'is_staff','is_teacher', 'science')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_teacher', 'science')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email','username','science')
    ordering = ('username','email','science')

admin.site.register(User,CustomUserAdmin)
