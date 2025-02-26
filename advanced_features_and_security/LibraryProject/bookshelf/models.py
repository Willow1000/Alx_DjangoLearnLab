from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author  = models.CharField(max_length=100)
    publication_year = models.DateField()


class CustomUserManager(BaseUserManager):
    def __init__(self):
        self.date_of_birth = models.DateField()
        self.profile_photo = models.ImageField(upload_to='profile_photos', blank=True)
    def create_user(self):
        self.objects.create_user(date_of_birth=self.date_of_birth,profile_photo=self.profile_photo)

    def create_superuser(self):
        self.objects.create_superuser(date_of_birth=self.date_of_birth,profile_photo=self.profile_photo)



class CustomUser(AbstractUser):
    objects = CustomUserManager()
    def can_create(self):
        return self.has_perm("bookshelf.can_add_book")

    def can_add(self):
        return self.has_perm("bookshelf.can_change_book")
    def can_edit(self):
        return self.has_perm("bookshelf.can_delete_book")
    def can_delete(self):
        return self.has_perm("bookshelf.can_delete_book")

