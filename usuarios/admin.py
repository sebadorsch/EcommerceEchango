from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'nombre', 'apellido']


admin.site.register(models.UserProfile, UserAdmin)

# admin.site.register(UserAdmin)
