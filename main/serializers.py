from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Comment, Subscriber

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Adjust fields as necessary
class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer()  # Use UserSerializer for nested representation
    title_image = serializers.SerializerMethodField()

    def get_title_image(self, obj):
        if isinstance(obj, dict):
            # If obj is a dictionary, it's likely during deserialization
            title_image = obj.get('title_image')
            if title_image and hasattr(title_image, 'url'):
                return title_image.url
            return title_image  # Return as is if it's already a URL string
        elif hasattr(obj, 'title_image'):
            # If obj is a model instance
            if obj.title_image:
                return obj.title_image.url
        return None  # Return None if title_image is not set or invalid

    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'category', 'title_image', 'content', 'author', 'date_posted']

class PaginatedBlogSerializer(serializers.Serializer):
    totalPosts = serializers.IntegerField()
    totalPages = serializers.IntegerField()
    currentPage = serializers.IntegerField()
    posts = BlogSerializer(many=True)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'content', 'date_posted']


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'email', 'date_subscribed']


class CategorySerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.CharField()
