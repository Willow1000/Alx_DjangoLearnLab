from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","publication_year")
    list_filter = ("publication_year")
    search_fields = ("title","author")
admin.site.register(Book)

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    list_display = ("profile_photo","date_of_birth")
    list_filter = ("date_of_birth")
    search_fields = ("profile_photo","date_of_birth")
