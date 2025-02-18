from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view: Accessible only to Admins
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin! You have access to the Admin section.")
