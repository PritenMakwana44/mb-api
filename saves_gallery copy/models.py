from django.db import models
from django.contrib.auth.models import User
from gallery.models import Gallery


class Save_gallery(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery = models.ForeignKey(
        Gallery, related_name='saved_gallery', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'gallery']

    def __str__(self):
        return f'{self.owner} {self.gallery}'