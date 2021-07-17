from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'avatar', 'email', 'date_joined', 'login', 'last_login', 'is_active']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="100" height="100"')

    get_image.short_description = "Изображение"