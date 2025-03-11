from django.shortcuts import render
from rest_framework import generics
from .models import *
from rest_framework.filters import OrderingFilter,SearchFilter
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
# from rest_framework.mixins 


# Create your views here.
# Retrieves all books
class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend,OrderingFilter,SearchFilter]
    search_fields = ['author','title','publication_year']
    ordering_fields = ['title','publication_year']

# Retrieve specific book using ID
class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class =  BookSerializer

# creates a new book
class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Updates record of existing book
class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

