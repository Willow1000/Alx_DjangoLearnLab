from .models import Author, Book, Library, Librarian

books = Book.objects.get(author=Author.objects.get(name="specific name").name)
print(books.all())

author_name='name'
Author.objects.get(name=author_name)

library_name='name'
Library.objects.get(name=library_name)
print(Librarian.objects.get(library=library_name))