from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

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


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view: Accessible only to Admins
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

# Librarian view: Accessible only to Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

# Member view: Accessible only to Members
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")

      