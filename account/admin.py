# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

@admin.register(User)
class userAdmin(admin.ModelAdmin):
       list_display = ['firstname','lastname','email','last_login','is_active',]
       ordering = ['firstname','lastname']

