from django.db import IntegrityError
from rest_framework import serializers
from gallerysaves.models import GallerySave


class GallerySaveSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GallerySave
        fields = [
            'id', 'created_on', 'owner', 'galleryposts']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate?'
            })