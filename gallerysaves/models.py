from django.db import models
from django.contrib.auth.models import User
from galleryposts.models import GalleryPost


class GallerySave(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    galleryposts = models.ForeignKey(
        GalleryPost, related_name='gallerysaved', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'galleryposts']

    def __str__(self):
        return f'{self.owner} {self.posts}'