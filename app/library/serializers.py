from rest_framework import serializers

from .models import (
    Book,
    Library,
    Author,
    Page,
)

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author"""

    class Meta:
        model = Author
        fields = '__all__'