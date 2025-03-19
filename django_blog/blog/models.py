from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now
from taggit.managers import TaggableManager

# User Manager
class AuthorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    

# Custom User Model
class Author(AbstractUser):
    ROLE_CHOICES = (("Admin", "Admin"), ("Blogger", "Blogger"), ("Viewer", "Viewer"))
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="Viewer")
    objects = AuthorManager()   
    user_permissions = models.ManyToManyField(Permission, related_name="Author_permission")
    groups = models.ManyToManyField(Group, related_name="Author_group")


# Like Model
class Like(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)  # Added relation
    time = models.DateTimeField(default=now)


# Links Model
class Links(models.Model):
    keyword = models.CharField(max_length=100)
    url = models.URLField(max_length=100)


# Post Model
class Post(models.Model):
    CATEGORY_CHOICES = (
        ("Beauty", "Beauty"),
        ("Lifestyle", "Lifestyle"),
        ("Food", "Food"),
        ("Finance", "Finance"),
        ("Relationships", "Relationships"),
        ("Career", "Career"),
    )

    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=5000)
    cover_image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogger")
    relevant_links = models.ManyToManyField(Links, blank=True)  # Uncommented
    tags = TaggableManager()  # Added

    def __str__(self):
        return self.title


# Comment Model
class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
