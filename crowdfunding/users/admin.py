from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# add CustomUserAdmin here (DM)

# Register your models here.

admin.site.register(CustomUser)