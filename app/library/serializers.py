from rest_framework import serializers

from .models import (
    Book,
    Library,
    Author,
    Page,
)

class LibrarySerializer(serializers.ModelSerializer):
    """Serializer for library"""

    class Meta:
        model = Library
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author"""

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Serializer for book"""
    library = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    authors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = ('id', 'title', 'library', 'authors')