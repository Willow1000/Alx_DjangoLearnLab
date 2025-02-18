from django.urls import path

from .views import list_books, LibraryDetailView

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
]