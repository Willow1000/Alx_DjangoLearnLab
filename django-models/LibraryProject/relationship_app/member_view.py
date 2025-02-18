from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Member view: Accessible only to Members
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member! You have access to the Member section.")
