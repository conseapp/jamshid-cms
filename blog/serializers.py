from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    # object_id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # object_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # comment = CommentSerializer()

    class Meta:
        model = Post
        fields = '__all__'
