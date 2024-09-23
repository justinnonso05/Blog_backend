# storage.py
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
import base64
from io import BytesIO

class DatabaseStorage(Storage):
    def _save(self, name, content):
        # Read the file content and encode it as base64
        data = base64.b64encode(content.read()).decode('utf-8')
        # Format it as a data URL (this can be adjusted for image types)
        return f"data:image/{name.split('.')[-1]};base64,{data}"

    def _open(self, name, mode='rb'):
        if name.startswith('data:'):
            # Extract base64 data and decode it to binary content
            _, data = name.split(',', 1)
            return ContentFile(base64.b64decode(data))
        return ContentFile(b'')

    def url(self, name):
        # Return the name as it contains the data URI
        return name

    def exists(self, name):
        # No files are actually stored, so always return False
        return False

    def get_valid_name(self, name):
        return name

    def size(self, name):
        if name.startswith('data:'):
            # Calculate size of base64-decoded data
            _, data = name.split(',', 1)
            return len(base64.b64decode(data))
        return 0
