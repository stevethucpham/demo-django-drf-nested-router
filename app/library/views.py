from django.shortcuts import render
from rest_framework import status, viewsets

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """Author ViewSet"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

