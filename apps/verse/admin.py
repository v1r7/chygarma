from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.verse.models import Category, Verse, Tag, Comment, Author, AuthorProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'content', 'tags',  'description', 'recommend', 'get_image']


    list_filter = ['pubdate', ]

    def get_image(self, obj):
        if obj.picture:
            return mark_safe(f'<img src={obj.picture.url} width="100" height="100"')
        return '-'

    get_image.short_description = "Изображение"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']

@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['id']
    filter_horizontal = ['readers']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content',  'verse']

