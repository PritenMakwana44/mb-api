from django.db import IntegrityError
from rest_framework import serializers
from save.models import Save


class SaveSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = [
            'id', 'created_on', 'owner', 'posts', 'galleryposts']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate?'
            })