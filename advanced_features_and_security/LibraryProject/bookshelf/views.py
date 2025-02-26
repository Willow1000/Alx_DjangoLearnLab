from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_add_book',raise_exception=True)
def add_book(request):
    return render(request, "add_book.html")


boo_list