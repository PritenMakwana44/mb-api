from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Saves(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(
        Post, related_name='saved', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'posts']

    def __str__(self):
        return f'{self.owner} {self.posts}'