from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.verse.models import Category, Verse, Picture, Author, Tag



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    fields = ['name',  'content', 'tags', 'description', 'authors', 'recommend', 'picture']




@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['get_image',]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = "Изображение"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', ]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]

