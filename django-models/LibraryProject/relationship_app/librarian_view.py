from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Librarian view: Accessible only to Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian! You have access to the Librarian section.")
