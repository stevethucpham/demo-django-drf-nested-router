from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.exceptions import NotFound

from .models import Author, Book, Library
from .serializers import (
    AuthorSerializer, BookSerializer, LibrarySerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    """Author ViewSet"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Book Viewset"""
    queryset = Book.objects.all().select_related(
        'library'
        ).prefetch_related(
            'authors'
        )
    serializer_class = BookSerializer
    
    def get_queryset(self, *args, **kwargs):
        library_id = self.kwargs.get("library_id")
        try:
            library = Library.objects.get(id=library_id)
        except Library.DoesNotExist:
            raise NotFound('A library with this id does not exist')
        return self.queryset.filter(library=library)


class LibraryViewSet(viewsets.ModelViewSet):
    """Library Viewset"""
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer