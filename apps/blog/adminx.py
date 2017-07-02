# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from .models import Category
from .models import Tag
from .models import Article
from .models import ImageLib

__author__ = "Eilene HE"
__date__ = '2017/6/26 10:08'


class CategoryAdmin(object):
    list_display = ['name', 'created_time']
    search_fields = ['name']
    list_filter = ['name', 'created_time']


class TagAdmin(object):
    list_display = ['name', 'created_time']
    search_fields = ['name']
    list_filter = ['name', 'created_time']


class ArticleAdmin(object):
    list_display = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author']
    search_fields = ['title', 'body', 'excerpt', 'category', 'tags', 'author']
    list_filter = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author']


class ImageLibAdmin(object):
    list_display = ['name', 'image', 'article', 'created_time']
    search_fields = ['name', 'article']
    list_filter = ['name', 'article', 'image']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ImageLib, ImageLibAdmin)
