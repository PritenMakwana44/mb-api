from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from mb_api.permissions import IsOwnerOrReadOnly
from .models import GalleryComment
from .serializers import GalleryCommentSerializer
from .serializers import GalleryCommentDetailSerializer


class GalleryCommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment in gallery posts if logged in.
    """
    serializer_class = GalleryCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GalleryComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gallerypost']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GalleryCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a Gallery comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GalleryCommentDetailSerializer
    queryset = GalleryComment.objects.all()
