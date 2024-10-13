from django.contrib import admin
from .models import Category, Post

# Register your models here.

# Configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Ensure that this is a tuple

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
