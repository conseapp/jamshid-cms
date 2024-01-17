from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Create your views here.

class Posts():
    pass
