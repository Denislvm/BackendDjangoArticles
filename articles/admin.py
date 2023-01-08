from django.contrib import admin

from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamp',
                    'update', 'publish']
    search_fields = ['title', 'content']


admin.site.register(Articles, ArticleAdmin)