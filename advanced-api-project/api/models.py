from django.db import models

# Create your models here.
# Author Model:
# stores info on authors
# has an attribute author which has a one to many relationship with the Book Model
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# Book Model:
# Keeps info on books
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.DateField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)