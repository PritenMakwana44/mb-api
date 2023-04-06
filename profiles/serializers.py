from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """Check if user is same as owner"""
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """Get following count for user"""
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """Meta class for model and fields"""
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'fav_tech', 'tech_bio', 'image', 'is_owner',
            'following_id', 'following_count', 'followers_count',
            'posts_count'
        ]
