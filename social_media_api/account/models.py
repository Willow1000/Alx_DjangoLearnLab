from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a regular user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)  # Normalize email (lowercase)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)  # Save to database
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a superuser with all permissions."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):

    bio = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to="profile_pic/",null=True,blank=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name="followers")
    objects = UserManager
    permissions = models.ManyToManyField(Permission,related_name="user_permissions")
    groups = models.ManyToManyField(Group,related_name="user_group")

    def __str__(self):
        return self.username
