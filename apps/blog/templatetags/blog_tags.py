# -*- coding: utf-8 -*-
from django import template
from django.db.models import Count
from ..models import Article
from ..models import Category

__author__ = "Eilene HE"
__date__ = '2017/6/26 14:51'


register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_archives():
    return Article.objects.datetimes('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_article=Count('article')).filter(num_article__gt=0)




