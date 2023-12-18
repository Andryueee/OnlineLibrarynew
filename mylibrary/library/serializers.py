# library/serializers.py

from rest_framework import serializers
from .models import Author, Book, Cover

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
