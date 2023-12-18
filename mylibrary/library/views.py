# library/views.py

from rest_framework import viewsets
from .models import Author, Book, Cover
from .serializers import AuthorSerializer, BookSerializer, CoverSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CoverViewSet(viewsets.ModelViewSet):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer
