from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import BookSerializer
# from rest_framework.mixins 


# Create your views here.
# Retrieves all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve specific book using ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class =  BookSerializer

# creates a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Updates record of existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

