from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Adjust fields as necessary
class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer()  # Use UserSerializer for nested representation
    title_image = serializers.SerializerMethodField()

    def get_title_image(self, obj):
        return obj.title_image.url 

    class Meta:
        model = Blog
        fields = ['id', 'title', 'category', 'title_image', 'content', 'author', 'date_posted']
