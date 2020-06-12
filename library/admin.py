from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
