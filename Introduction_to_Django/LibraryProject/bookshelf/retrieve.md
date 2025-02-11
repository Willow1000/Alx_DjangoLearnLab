# Code
book = Book.objects.get(author="1984")
print(book.title)
print(book.author)
print(book.publication_year)

# Output
1984
George Orwell
1949