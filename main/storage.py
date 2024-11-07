from django.core.files.storage import Storage
from django.core.files.base import ContentFile
import cloudinary
import cloudinary.uploader
from io import BytesIO
import base64
import re

class DatabaseStorage(Storage):
    def _open(self, name, mode='rb'):
        if name.startswith('data:'):
            data = name.split(',', 1)[1]
            return ContentFile(base64.b64decode(data))
        return ContentFile(b"")

    def _save(self, name, content):
        try:
            if hasattr(content, 'read'):
                file_content = content.read()
            else:
                file_content = content

            result = cloudinary.uploader.upload(
                file_content,
                folder="Blog/content",
                resource_type="auto",
                unique_filename=True
            )
            
            # Clean the URL to ensure no unwanted characters
            clean_url = self._clean_url(result['secure_url'])
            return clean_url

        except Exception as e:
            print(f"Cloudinary upload error: {str(e)}")
            raise e

    def _clean_url(self, url):
        # Remove any backslashes and extra characters after .jpg/.png/etc
        if url:
            # Match until the end of the image extension
            pattern = r'(.*?\.(jpg|jpeg|png|gif|webp|svg))'
            match = re.match(pattern, url, re.IGNORECASE)
            if match:
                return match.group(1)
            return url.split('\\')[0]  # Fallback: just remove backslashes
        return url

    def exists(self, name):
        return False

    def get_valid_name(self, name):
        return name

    def url(self, name):
        # Clean the URL before returning
        return self._clean_url(name)

    def size(self, name):
        return 0

    def deconstruct(self):
        return ('main.storage.DatabaseStorage', [], {})



# from django.core.files.storage import Storage
# from django.core.files.base import ContentFile
# import base64
# from io import BytesIO

# class DatabaseStorage(Storage):
#     def _open(self, name, mode='rb'):
#         if name.startswith('data:'):
#             data = name.split(',', 1)[1]
#             return ContentFile(base64.b64decode(data))
#         return ContentFile(b"")

#     def _save(self, name, content):
#         data = base64.b64encode(content.read()).decode('utf-8')
#         return f"data:image/{name.split('.')[-1]};base64,{data}"

#     def exists(self, name):
#         return False

#     def get_valid_name(self, name):
#         return name

#     def url(self, name):
#         return name

#     def size(self, name):
#         if name.startswith('data:'):
#             data = name.split(',', 1)[1]
#             return len(base64.b64decode(data))
#         return 0

#     def deconstruct(self):
#         return ('main.storage.DatabaseStorage', [], {})
