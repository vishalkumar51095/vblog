from django.contrib import admin

from .models import Category, Post
from django.db import models

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
