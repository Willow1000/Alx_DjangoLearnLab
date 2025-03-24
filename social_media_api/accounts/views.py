from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class RegisterUserView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy("home")
    model = User

class LoginUserView(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("home")

class UserProfileView(DetailView):
    template_name = "profile,html"
    model = User
    context_object_name = "blog"  

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

