from django.contrib import admin

from .models import Author, Book



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author__name')
    autocomplete_fields = ('author',)


admin.site.register(Author)    
admin.site.register(Book)
