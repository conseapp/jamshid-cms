from django.shortcuts import render
from .serializers import CategorySerializer, CommentSerializer, PostSerializer
from .models import Post, Category, Comment
from rest_framework import generics


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs.get('category')  # Retrieve the 'category' parameter from the URL
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class CommentListByPostAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(content_type__model='post', object_id=post_id)
