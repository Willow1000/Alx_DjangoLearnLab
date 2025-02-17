from .models import Author, Book, Library, Librarian

print(Book.objects.filter(author='specific_author'))
print(Library.objects.all())
library_name = Library.objects.get('name')
print(Librarian.objects.get(library=library_name))