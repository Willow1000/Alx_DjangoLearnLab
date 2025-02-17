from .models import Author, Book, Library, Librarian

print(Book.objects.filter(author='specific_author'))
print(Library.objects.all())
print(Librarian.objects.get(library=Library.objects.get('name')))