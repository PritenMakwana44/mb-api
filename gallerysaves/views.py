from rest_framework import generics, permissions
from mb_api.permissions import IsOwnerOrReadOnly
from gallerysaves.models import GallerySave
from gallerysaves.serializers import GallerySaveSerializer


class GallerySaveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GallerySaveSerializer
    queryset = GallerySave.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GallerySaveDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GallerySaveSerializer
    queryset = GallerySave.objects.all()


