from django.contrib import admin

from .models import Tag, Article

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "author", "tag", "photo",)
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
