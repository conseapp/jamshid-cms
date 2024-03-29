from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="posts"),
    path('post/<str:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('category/<str:slug>/', views.PostListView.as_view(), name='post-list-by-category'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('post/<str:slug>/comments/', views.CommentListByPostAPIView.as_view(), name='comments-by-post'),
]

