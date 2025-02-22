from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/templates/relationship_app/library_detail.html'
    content_type = 'library'

class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/templates/relationship_app/register.html'

class LoginView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/templates/relationship_app/login.html'    

class LogoutView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('logout')  
    template_name = 'relationship_app/templates/relationship_app/logout.html'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Librarian view: Accessible only to Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian! You have access to the Librarian section.")


# Function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view: Accessible only to Admins
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin! You have access to the Admin section.")


# Function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Member view: Accessible only to Members
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member! You have access to the Member section.")

      

# Add Book View
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit Book View
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# Delete Book View
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})
