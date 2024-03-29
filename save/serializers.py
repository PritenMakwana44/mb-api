from django.db import IntegrityError
from rest_framework import serializers
from save.models import Save


class SaveSerializer(serializers.ModelSerializer):
    """Serializer for save model"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta for model and fields for save"""
        model = Save
        fields = [
            'id', 'created_on', 'owner', 'posts']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate?'
            })
