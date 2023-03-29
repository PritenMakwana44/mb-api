from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from mb_api.permissions import IsOwnerOrReadOnly
from .models import Comment_gallery
from .serializers import Comment_gallerySerializer, Comment_galleryDetailSerializer


class Comment_galleryList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = Comment_gallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment_gallery.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gallery']

    def perform_create(self, serializer):
        serializer.save_gallery(owner=self.request.user)


class Comment_galleryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = Comment_galleryDetailSerializer
    queryset = Comment_gallery.objects.all()