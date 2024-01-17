from django.db import models
import uuid


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='post_images')
    body = models.TextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=11)
