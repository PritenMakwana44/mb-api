from rest_framework import generics, permissions
from mb_api.permissions import IsOwnerOrReadOnly
from saves.models import Saves
from saves.serializers import SavesSerializer


class SavesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavesSerializer
    queryset = Saves.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavesSerializer
    queryset = Saves.objects.all()