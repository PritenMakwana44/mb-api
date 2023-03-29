from rest_framework import serializers
from gallery.models import Gallery
from saves_gallery.models import Save_gallery


class GallerySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_gallery_id = serializers.SerializerMethodField()
    save_gallery_count = serializers.ReadOnlyField()
    comments_gallery_count = serializers.ReadOnlyField()

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

    def get_save_gallery_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save_gallery = Save_gallery.objects.filter(
                owner=user, gallery=obj
            ).first()
            return save_gallery.id if save_gallery else None
        return None

    class Meta:
        model = Gallery
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'item_list', 'image',
            'save_gallery_id', 'save_gallery_count', 
            'comments_gallery_count',
        ]