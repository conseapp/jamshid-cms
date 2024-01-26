from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Post, Category, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget(config_name='custom_ckeditor')},
    }
    readonly_fields = ['post_id', 'created_at', 'updated_at', 'image_tag']
    list_display = ['title', 'custom_body', 'category', 'updated_at', 'is_published']
    search_fields = ['title']
    fieldsets = (
        (_(""), {'fields': (
            'title', 'body', 'image', 'image_tag', 'category', 'slug', 'is_published', 'created_at', 'updated_at',
            'post_id')}),
    )
    actions = ('set_published', 'set_unpublished',)

    def image_tag(self, obj):
        return format_html(
            '<img style="width:300px" src="{}" />'.format(obj.image.url))

    def render_html_content(self, obj):
        return format_html(obj.body)

    def custom_body(self, obj):
        return obj.extracted_body

    @admin.action(description='publish selected posts')
    def set_published(modeladmin, request, queryset):
        for obj in queryset:
            obj.is_published = True
            obj.save()
        messages.success(request, "Successfully published!")

    @admin.action(description='unpublish selected posts')
    def set_unpublished(modeladmin, request, queryset):
        for obj in queryset:
            obj.is_published = False
            obj.save()
        messages.success(request, "Successfully unpublished!")

    render_html_content.short_description = 'body'
    custom_body.short_description = 'body'
    image_tag.short_description = 'Image preview'
    image_tag.allow_tags = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['id']
    list_display = ['model_str', 'parent', 'post_count', 'id']

    def model_str(self, obj):
        return str(obj)

    def post_count(self, obj):
        return obj.post.count()

    model_str.short_description = 'Category'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'author', 'created_at', 'generic_obj', 'is_published']

    def generic_obj(self, obj):
        generic_object = obj.content_object
        return generic_object
