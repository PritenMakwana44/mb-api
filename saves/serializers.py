from django.db import IntegrityError
from rest_framework import serializers
from saves.models import Saves


class SavesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Saves
        fields = [
            'id', 'created_on', 'owner', 'posts']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplicate?'
            })