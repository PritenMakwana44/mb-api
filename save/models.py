from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from galleryposts.models import GalleryPost


class Save(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(
        Post, related_name='saved', on_delete=models.CASCADE)
    galleryposts = models.ForeignKey(
        GalleryPost, related_name='saved', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'posts']
        unique_together = ['owner', 'galleryposts']

    def __str__(self):
        return f'{self.owner} {self.posts}'
        return f'{self.owner} {self.galleryposts}'