from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CommentListView, SubscriberListCreate, unsubscribe, CategoryListView

urlpatterns = [
    path('api/blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('api/blogs/detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('api/blogs/comments/', CommentListView.as_view(), name='blog-comment'),
    path('api/subscribe/', SubscriberListCreate.as_view(), name='suscribe'),
    path('unsubscribe/<uuid:token>/', unsubscribe, name='unsubscribe'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    # path('admin/upload-image/', upload_image, name='upload_image'),
]
