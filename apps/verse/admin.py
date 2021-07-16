from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.verse.models import Category, Verse, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ['name',  'content', 'tags', 'description', 'recommend', 'get_image']

    list_filter = ['pubdate', ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="100" height="100"')

    get_image.short_description = "Изображение"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content',  'verse']

