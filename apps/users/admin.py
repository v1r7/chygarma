from django.contrib import admin

# Register your models here.
from apps.users.models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'date_joined', 'login', 'last_login', 'is_active']