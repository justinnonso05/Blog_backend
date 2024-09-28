from django.urls import path
from .views import BlogListCreateView

urlpatterns = [
    path('api/blogs/', BlogListCreateView.as_view(), name='blog-list'),
    # path('admin/upload-image/', upload_image, name='upload_image'),
]
