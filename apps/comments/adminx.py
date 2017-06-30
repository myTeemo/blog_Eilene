# -*- coding: utf-8 -*-
import xadmin

from .models import Comment
from .models import Contact

__author__ = "Eilene HE"
__date__ = '2017/6/26 17:40'


class CommentsAdmin(object):
    list_display = ['name', 'email', 'url', 'text', 'created_time', 'article']
    search_fields = ['name', 'email', 'url', 'article']
    list_filter = ['name', 'email', 'url', 'text', 'created_time', 'article']


class ContactAdmin(object):
    list_display = ['name', 'email', 'subject', 'created_time', 'text']
    search_fields = ['name', 'email', 'subject', 'text']
    list_filter = ['name', 'email', 'subject', 'text']


xadmin.site.register(Comment, CommentsAdmin)
xadmin.site.register(Contact, ContactAdmin)