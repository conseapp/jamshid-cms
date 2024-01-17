from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
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
    comment = GenericRelation("Comment", related_name="post")
    category = GenericRelation("Category", related_query_name='post')

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=11)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=200)
    content_object = GenericForeignKey('content_type', 'object_id')

    comment = GenericRelation("Comment", related_query_name='comment')

    def __str__(self):
        return self.body


class Category(models.Model):
    name = models.CharField(max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=200)
    content_object = GenericForeignKey('content_type', 'object_id')
    category = GenericRelation("Category", related_query_name='category')

    def __str__(self):
        return self.name
