from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs_detail', args=[str(self.id)])
