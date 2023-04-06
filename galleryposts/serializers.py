from rest_framework import serializers
from galleryposts.models import GalleryPost


class GalleryPostSerializer(serializers.ModelSerializer):
    """GalleryPost serializer"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    gallerycomments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        "Check values for size, width and height on Gallerypost images"
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
        """Check if user is the same as owner"""
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """Meta class for model and fields"""
        model = GalleryPost
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'item_list', 'image',
            'gallerycomments_count',
        ]
