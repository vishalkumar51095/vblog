from django.contrib import admin
from .models import Category, Post


# Register your models here.

# Configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description','url','add_date') 
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 1

    class Media:
        #  js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js')
        js = ('https://cdn.tiny.cloud/1/sql06tihabe7iu6yzzwyaw5xqbpse9xkgkhin1n26c0im13l/tinymce/5/tinymce.min.js', 'js/script.js')
    #     # js = ('js/script.js',)
    # class Media:
    #     js = (
    #         'https://cdn.ckeditor.com/ckeditor5/36.0.1/classic/ckeditor.js',  # CKEditor CDN
    #         'js/script.js',  # Your custom JS to initialize CKEditor
    #     )
    #     css = {
    #         'all': (
    #             'https://cdn.ckeditor.com/ckeditor5/36.0.1/classic/ckeditor.css',  # CKEditor CSS
    #         )
    #     }
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)
