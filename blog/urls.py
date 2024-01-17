from django.urls import path
from . import views
urlpatterns = [
    path("posts/", views.Posts.as_view(), name="posts"),
    path('post/<str:slug>', views.detail, name='detail')
]