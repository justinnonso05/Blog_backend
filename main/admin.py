from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import Blog, Comment
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment
from .forms import BlogForm


# Change the admin site texts
admin.site.site_header = _("Admin Dashboard")  # Change 'Django Administration'
admin.site.site_title = _("Admin Dashboard")  # Change 'Site Title'
admin.site.index_title = _("Welcome to the Admin Dashboard")  # Change 'Welcome to the Admin Index Page'


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Attachment)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Override fieldsets to exclude permissions
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # You can also exclude permissions from the forms if required
    exclude = ('groups', 'user_permissions')

# Apply summernote to all TextField in model.
class BlogAdmin(ModelAdmin, SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ('title', 'author', 'category')
    summernote_fields = ('content',)
    form = BlogForm
    
class CommentAdmin(ModelAdmin):  # instead of ModelAdmin
    list_display = ('name', 'content')
       

admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)

# admin.site.register(CloudinaryAttachment, AttachmentAdmin)