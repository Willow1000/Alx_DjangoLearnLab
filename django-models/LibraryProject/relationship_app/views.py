from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from .models import Library
# Create your views here.
def show_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class library_views(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    content_type = 'library'