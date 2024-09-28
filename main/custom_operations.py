# from django.db.migrations.operations.base import Operation

# class SetAttachmentStorageClass(Operation):
#     def state_forwards(self, app_label, state):
#         pass

#     def database_forwards(self, app_label, schema_editor, from_state, to_state):
#         from django.conf import settings
#         settings.SUMMERNOTE_CONFIG['attachment_storage_class'] = 'main.storage.DatabaseStorage'

#     def database_backwards(self, app_label, schema_editor, from_state, to_state):
#         from django.conf import settings
#         settings.SUMMERNOTE_CONFIG['attachment_storage_class'] = 'django.core.files.storage.FileSystemStorage'

#     def describe(self):
#         return "Set attachment storage class"
