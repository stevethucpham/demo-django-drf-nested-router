from django.contrib import admin
from .models import (
    Library,
    Book,
    Author,
)

class BookAdmin(admin.ModelAdmin):
    """Manage book"""
    list_display = ('title', 'library')

admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)