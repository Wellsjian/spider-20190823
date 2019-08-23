from django.contrib import admin

# Register your models here.
from . import models


# 添加自定义类让admin管理


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_house', 'price']
    list_display_links = ['id', 'title', 'pub_house', ]
    list_filter = ["pub_house"]
    search_fields = ['title', 'pub_house']
    list_editable = ['price']




admin.site.register(models.Book, BookManager)
admin.site.register(models.Author)
admin.site.register(models.Wife)
