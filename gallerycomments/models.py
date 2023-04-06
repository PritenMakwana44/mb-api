from django.db import models
from django.contrib.auth.models import User
from galleryposts.models import GalleryPost


class GalleryComment(models.Model):
    """
    Gallery Comment model, related to User and Gallery post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gallerypost = models.ForeignKey(GalleryPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
