from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import Book
from .forms import ExampleForm, BookForm

# View to add a new book (requires 'can_add_book' permission)
@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "bookshelf/book_list.html", {"message": "Book added successfully!"})
    else:
        form = BookForm()
    
    return render(request, "bookshelf/add_book.html", {"form": form})

# View to display the book list (requires 'can_view_book' permission)
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    query = request.GET.get("q", "")
    
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    
    return render(request, "bookshelf/book_list.html", {"books": books})
