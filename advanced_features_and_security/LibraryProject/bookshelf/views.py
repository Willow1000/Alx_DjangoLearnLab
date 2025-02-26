from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
# Create your views here.

@permission_required('bookshelf.can_add_book',raise_exception=True)
def add_book(request):
    return render(request, "add_book.html")


book_list