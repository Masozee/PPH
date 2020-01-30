# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import CustomUser, Visitor


admin.site.register(CustomUser)
admin.site.register(Visitor)