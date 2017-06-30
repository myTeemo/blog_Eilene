# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import PostCommentView
from .views import PostContactView

__author__ = "Eilene HE"
__date__ = '2017/6/26 21:10'


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<pk>[0-9]+)/$', PostCommentView.as_view(), name='post_comment'),
    url(r'^contact/post/$',PostContactView.as_view(), name="post_contact"),
]
