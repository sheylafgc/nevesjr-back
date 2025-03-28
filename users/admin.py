from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, 
            {
                'fields': (
                    'first_name', 
                    'last_name', 
                    'email', 
                    'password',
                    'phone',
                    'title',
                )
            }
        ),
        ('Permissions', 
            {
                'fields': (
                    'is_staff', 
                    'is_active',
                )
            }
        ),
    )
    add_fieldsets = (
        (None, 
        {
            'classes': ('wide',),
            'fields': (
                'first_name', 
                'last_name', 
                'email', 
                'password',
                'phone',
                'title',
            )
        }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
