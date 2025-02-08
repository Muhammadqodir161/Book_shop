from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price', 'created_at')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre',)
