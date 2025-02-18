from .models import Author, Book, Library, Librarian

books = Book.objects.get(author=Author.objects.get(name="specific name").name)
print(books.all())

library = Library.objects.get(id=1)
print(library.all())

library_name='name'
Library.objects.get(name=library_name)
print(Librarian.objects.get(library=library_name))