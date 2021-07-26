from django.contrib import admin
from .models import Category, Page
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'views', 'likes']
    list_display_links = ['name',]
    list_editable = ['views', 'likes',]
    prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']#, 'views']
    list_display_links = ['title',]
    # list_editable = ['category', 'url']

    list_filter = ['category',]
    # search_fields = ['category__name', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
