from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library

# Create your views here.
def show_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class library_views(ListView):
    model = Library
    template_name = 'relationship_app/library_details.html'
    content_type = 'library'