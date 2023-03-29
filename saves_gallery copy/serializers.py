from django.db import IntegrityError
from rest_framework import serializers
from saves_gallery.models import Save_gallery


class Save_gallerySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save_gallery
        fields = [
            'id', 'created_on', 'owner', 'gallery']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate?'
            })