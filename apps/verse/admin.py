from django.contrib import admin

from apps.verse.models import Category, Verse


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ['name', 'pubdate', 'content']
