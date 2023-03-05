from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Gallery
from .serializers import GallerySerializer
from mb_api.permissions import IsOwnerOrReadOnly


class GalleryPostList(APIView):
    """
    List posts or create a post if logged in
    """
    serializer_class = GallerySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        gallery = Gallery.objects.all()
        serializer = GallerySerializer(
            gallery, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def gallery(self, request):
        serializer = GallerySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class GalleryPostDetail(APIView):
    """
    Retrieve a post and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GallerySerializer

    def get_object(self, pk):
        try:
            gallery = Gallery.objects.get(pk=pk)
            self.check_object_permissions(self.request, gallery)
            return gallery
        except Gallery.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        gallery = self.get_object(pk)
        serializer = GallerySerializer(
            gallery, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        gallery = self.get_object(pk)
        serializer = GallerySerializer(
            gallery, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        gallery = self.get_object(pk)
        gallery.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )