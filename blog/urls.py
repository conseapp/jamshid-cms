from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="posts"),
    path('post/<str:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/category/<str:category>/', views.PostDetailView.as_view(), name='post-list-by-category'),
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('post/<str:slug>/comments/', views.CommentListByPostAPIView.as_view(), name='comments-by-post'),
]
