# blog/admin.py

from material.admin import MaterialAdminSite
from django.contrib import admin
from .models import Category, Post

# Use MaterialAdminSite for a better UI
admin.site = MaterialAdminSite()

# Configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10

# Register models with their respective admin configurations
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
