from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.show_books, name='books'),
    path('library/<int:pk>', views.library_views.as_view(), name='library_detail'),
]