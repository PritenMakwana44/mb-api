from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer for model"""

    class Meta:
        model = Contact
        fields = [
            'firstname',
            'lastname',
            'email',
            'content',
            'created_on',
        ]
