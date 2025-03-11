from django.urls import path,include
from rest_framework.routers import DefaultRouter
from views import *

router = DefaultRouter()
router.register()

urlpatterns = [
    path('/create',CreateView.as_view()),
    path('/books/',ListView.as_view()),
    path('/books/<int:pk>/',DetailView.as_view()),
    path('/books/update/<int:pk>/',UpdateView.as_view()),
    path('/books/delete/<int:pk>/',DeleteView.as_view()),
]