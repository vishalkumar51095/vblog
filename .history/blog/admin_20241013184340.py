# blog/admin.py

from django.contrib import admin
from .models import Category, Post
from material.admin import  MaterialModelAdmin

# Configuration of Category admin
class CategoryAdmin(MaterialModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class PostAdmin(MaterialModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10

# Register models with their respective admin configurations
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
