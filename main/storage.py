from django.core.files.storage import Storage
from django.core.files.base import ContentFile
import base64
from io import BytesIO

class DatabaseStorage(Storage):
    def _open(self, name, mode='rb'):
        if name.startswith('data:'):
            data = name.split(',', 1)[1]
            return ContentFile(base64.b64decode(data))
        return ContentFile(b"")

    def _save(self, name, content):
        data = base64.b64encode(content.read()).decode('utf-8')
        return f"data:image/{name.split('.')[-1]};base64,{data}"

    def exists(self, name):
        return False

    def get_valid_name(self, name):
        return name

    def url(self, name):
        return name

    def size(self, name):
        if name.startswith('data:'):
            data = name.split(',', 1)[1]
            return len(base64.b64decode(data))
        return 0

    def deconstruct(self):
        return ('main.storage.DatabaseStorage', [], {})
