from django.urls import path

from .views import list_books, LibraryDetailView
from . import admin_view, librarian_view, member_view
from . import views
from .views import *

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/<int:pk>',LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register.as_view(template_name='relationship_app/templates/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/templates/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/logout.html'), name='logout'),
    path('admin/', admin_view.admin_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_view, name='librarian_view'),
    path('member/', member_view.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]