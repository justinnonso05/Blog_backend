from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'category', 'title_image', 'content', 'date_posted']

    
