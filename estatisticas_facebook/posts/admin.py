from django.contrib import admin
from posts.models import *

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Post,PostAdmin)