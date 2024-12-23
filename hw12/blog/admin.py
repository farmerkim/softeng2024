from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'head_image')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)