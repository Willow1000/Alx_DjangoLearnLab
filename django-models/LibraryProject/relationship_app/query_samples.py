from .models import Author, Book, Library, Librarian

books = Book.objects.get(author=Author.objects.get(name="specific name").name)
print(books.all())

library = Library.objects.get(id=1)
print(library.all())

library_name=Library.objects.get(name="Library Name")
print(Librarian.objects.get(library=library_name))