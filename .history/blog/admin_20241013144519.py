from django.contrib import admin

from .models import Category, Post
from django.db import models

# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(Category)
admin.site.register(Post)
