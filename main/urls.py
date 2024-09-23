from django.urls import path
from .views import BlogListCreateView, BlogDetailView, upload_image

urlpatterns = [
    path('api/blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('api/blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('upload_image/', upload_image, name='upload_image'),
    # path('admin/upload-image/', upload_image, name='upload_image'),
]
