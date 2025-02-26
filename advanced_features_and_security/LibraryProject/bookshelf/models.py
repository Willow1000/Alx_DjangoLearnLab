from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author  = models.CharField(max_length=100)
    publication_year = models.DateField()


class User(AbstractUser):
    def __init__(self):
        self.date_of_birth = models.DateField()
        self.profile_photo = models.ImageField(upload_to='profile_photos', blank=True)
    def create_user(self):
        user = User.objects.create_user(date_of_birth=self.date_of_birth,profile_photo=self.profile_photo)
        user.save()

    def create_super


