from django.db import models

# Create your models here.
class Author(models.Model):
    name=  models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="author")
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(Author,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(Author,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    