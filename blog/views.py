from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import CategorySerializer, CommentSerializer, PostSerializer
from .utils import CustomCommentPagination, CustomPostPagination
from rest_framework.response import Response

from rest_framework import status, filters
from .models import Post, Category, Comment
from .decorators import login_required


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'extracted_body']
    pagination_class = CustomPostPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('slug', None)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            if category:
                descendants = self.request.query_params.get('descendants', None)
                if descendants == "False":
                    queryset = queryset.filter(category=category)
                categories = category.get_descendants()
                categories.append(category)
                queryset = queryset.filter(category__in=categories)
        # return queryset.order_by('created_at').all() ## for ordering
        return queryset


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    search_fields = ['title', 'body']


class CommentListByPostAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = CustomCommentPagination

    def get_queryset(self):
        post_slug = self.kwargs['slug']
        post = Post.objects.get(slug=post_slug)
        return Comment.objects.filter(content_type__model='post', object_id=post.post_id)

    @login_required
    def create(self, request, *args, **kwargs):
        post_slug = self.kwargs['slug']
        post = Post.objects.get(slug=post_slug)
        content_type = ContentType.objects.get_for_model(post)
        request.data['content_type'] = content_type.id
        request.data['object_id'] = str(post.post_id)
        response = super().create(request, *args, **kwargs)

        return response
