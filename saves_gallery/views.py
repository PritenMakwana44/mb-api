from rest_framework import generics, permissions
from mb_api.permissions import IsOwnerOrReadOnly
from saves_gallery.models import Save_gallery
from saves_gallery.serializers import Save_gallerySerializer


class Save_galleryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Save_gallerySerializer
    queryset = Save_gallery.objects.all()

    def perform_create(self, serializer):
        serializer.save_gallery(owner=self.request.user)


class Save_galleryDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = Save_gallerySerializer
    queryset = Save_gallery.objects.all()