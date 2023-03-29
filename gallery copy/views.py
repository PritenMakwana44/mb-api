from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from mb_api.permissions import IsOwnerOrReadOnly
from .models import Gallery
from .serializers import GallerySerializer


class GalleryList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.annotate(
        save_gallery_count=Count('saved_gallery', distinct=True),
        comments_gallery_count=Count('comment_gallery', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'saved_gallery__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'save_gallery_count',
        'comments_gallery_count',
        'save_gallery__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save_gallery(owner=self.request.user)


class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = GallerySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Gallery.objects.annotate(
        save_gallery_count=Count('saved_gallery', distinct=True),
        comments_gallery_count=Count('comment_gallery', distinct=True)
    ).order_by('-created_at')