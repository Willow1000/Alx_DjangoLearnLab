import rest_framework
from .models import Book

class BookSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'created_at', 'updated_at']