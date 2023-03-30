from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from mb_api.permissions import IsOwnerOrReadOnly
from .models import GalleryPost
from .serializers import GalleryPostSerializer


class GalleryPostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = GalleryPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = GalleryPost.objects.annotate(
        gallerysave_count=Count('gallerysaved', distinct=True),
        gallerycomments_count=Count('gallerycomment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'gallerysaved__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'gallerysave_count',
        'gallerysave__created_at',
    ]

    def perform_create(self, serializer):
        serializer.gallerysave(owner=self.request.user)


class GalleryPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = GalleryPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = GalleryPost.objects.annotate(
        gallerysave_count=Count('gallerysaved', distinct=True),
        gallerycomments_count=Count('gallerycomment', distinct=True)
    ).order_by('-created_at')

    def post(self, request, pk):
        serializer = GalleryPostSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            print(serializer.errors)