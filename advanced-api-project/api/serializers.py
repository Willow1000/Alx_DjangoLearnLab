from rest_framework import serializers
from .models import *
from django.utils.timezone import now
# BookSerializer
# Converts Book model to simple json/xml/html format 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Ensures publication year is not in future
    def validate(self, attrs):
        if attrs['publication'] > now().date():
            raise serializers.ValidationError("Publication Year Can Not Be In The Future")
        return attrs
class AuthorSerializer(serializers.ModelSerializer):
    # nested serializer
    book = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = ["name"]    

   