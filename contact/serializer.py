from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Contact
        fields = [
            'firstname',
            'lastname',
            'email',
            'content',
            'created_on',
        ]