from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PostResource(resources.ModelResource):

    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource
    
admin.site.register(Post)
