from rest_framework import serializers
from .models import Liquor

class LiquorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Liquor
        fields = ('id', 'name', 'category', 'price', 'can_or_bottle', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')