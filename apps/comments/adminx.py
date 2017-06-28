# -*- coding: utf-8 -*-
import xadmin

from .models import Comment

__author__ = "Eilene HE"
__date__ = '2017/6/26 17:40'


class CommentsAdmin(object):
    list_display = ['name', 'email', 'url', 'text', 'created_time', 'article']
    search_fields = ['name', 'email', 'url', 'article']
    list_filter = ['name', 'email', 'url', 'text', 'created_time', 'article']


xadmin.site.register(Comment, CommentsAdmin)