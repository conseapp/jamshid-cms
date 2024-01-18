from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['post_id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['id']
    ...


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
