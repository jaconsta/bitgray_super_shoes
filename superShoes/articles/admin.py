from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store_name', 'total_in_shelf', 'total_in_vault')

    def store_name(self, object):
        return object.store.name


admin.site.register(Article, ArticleAdmin)
