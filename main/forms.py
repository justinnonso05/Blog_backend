from django import forms
from .models import Blog
import base64

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'title', 'category', 'title_image', 'content', 'date_posted']

    def clean_content(self):
        content = self.cleaned_data['content']

        # Find and process images in the content
        if 'src="' in content:
            img_tags = content.split('src="')[1:]  # Split and get image tags
            for img_tag in img_tags:
                base64_data = img_tag.split('"')[0]  # Extract Base64 data
                if base64_data.startswith('data:image/'):
                    # Process the Base64 image data
                    # This part could be customized as needed
                    # For example, you can validate image size or type here
                    content = content.replace(base64_data, base64_data)

        return content
