from rest_framework import serializers
from galleryposts.models import GalleryPost
from gallerysaves.models import GallerySave


class GalleryPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    gallerysave_id = serializers.SerializerMethodField()
    gallerysave_count = serializers.ReadOnlyField()
    gallerycomments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_gallerysave_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            gallerysave = GallerySave.objects.filter(
                owner=user, galleryposts=obj
            ).first()
            return gallerysave.id if gallerysave else None
        return None

    class Meta:
        model = GalleryPost
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'item_list', 'image',
            'gallerysave_id', 'gallerysave_count', 
            'gallerycomments_count',
        ]