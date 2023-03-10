from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.firstname} {self.lastname}'