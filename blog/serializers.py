from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    # comment = CommentSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def get_category(self, obj):
        return obj.category.name
