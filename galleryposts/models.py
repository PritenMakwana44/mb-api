from django.db import models
from django.contrib.auth.models import User


class GalleryPost(models.Model):
    """
    Gallery posts model and placeholder image for posts
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    item_list = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_bdqh5h', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
