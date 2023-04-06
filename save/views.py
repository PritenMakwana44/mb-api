from rest_framework import generics, permissions
from mb_api.permissions import IsOwnerOrReadOnly
from save.models import Save
from save.serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    """View for Save list for posts"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    """Detail View for Save list for posts"""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()
