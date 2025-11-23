from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters on the right-hand sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality
    search_fields = ('title', 'author')

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
