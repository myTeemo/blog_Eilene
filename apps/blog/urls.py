# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import ArticleDetailView
from .views import IndexView
from .views import ArchivesView
from .views import CategoryView
from .views import AboutView
from .views import ContactView
from .views import ImageLibView


__author__ = "Eilene HE"
__date__ = '2017/6/26 10:29'

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^article_detail/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name="article_detail"),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^images/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<image_address>.*)/$', ImageLibView.as_view(), name='image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
