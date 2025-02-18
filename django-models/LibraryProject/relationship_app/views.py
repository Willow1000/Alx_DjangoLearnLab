from django.shortcuts import render
from .models import Book

# Create your views here.
def show_books(request):
    books = Book.objects.all()
    return books