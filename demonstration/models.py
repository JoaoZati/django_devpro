from django.db import models
from django.urls import reverse


class Video(models.Model):
    slug = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('demonstration:video', args=(self.slug,))

    def __str__(self):
        return f'Video: {self.title}'
