from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CommentListView, SubscriberListCreate

urlpatterns = [
    path('api/blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('api/blogs/detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('api/blogs/comments/', CommentListView.as_view(), name='blog-comment'),
    path('api/subscribe/', SubscriberListCreate.as_view(), name='suscribe'),
    # path('admin/upload-image/', upload_image, name='upload_image'),
]
