from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    breadcrumbs = serializers.SerializerMethodField()
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_breadcrumbs(self, obj):
        return str(obj)

    def get_parent(self, obj):

        return str(obj.parent.name) if obj.parent else None


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    # comment = CommentSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def get_category(self, obj):
        # return str(obj.category)
        return obj.category.name

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def get_updated_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")
