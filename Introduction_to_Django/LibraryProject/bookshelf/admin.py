from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('author', 'publication_year')  # Filters to add on the sidebar
    search_fields = ('title', 'author')  # Fields to include in the search bar

admin.site.register(Book, BookAdmin)
