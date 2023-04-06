from rest_framework import serializers
from posts.models import Post
from save.models import Save


class PostSerializer(serializers.ModelSerializer):
    """Post serializer"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()
    save_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        "Check values for size, width and height on post images"
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

    def get_save_id(self, obj):
        """return save count per user"""
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, posts=obj
            ).first()
            return save.id if save else None
        return None

    class Meta:
        """Meta class for model and fields"""
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'type', 'year',
            'save_id', 'save_count', 'comments_count',
        ]
