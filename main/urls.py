from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CommentListView

urlpatterns = [
    path('api/blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('api/blogs/detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('api/blogs/comments/', CommentListView.as_view(), name='blog-comment'),
    # path('admin/upload-image/', upload_image, name='upload_image'),
]
