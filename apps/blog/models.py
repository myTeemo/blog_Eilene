# -*- encoding:utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile


class Category(models.Model):
    name = models.CharField(verbose_name=u'分类', max_length=100)
    created_time = models.DateTimeField(verbose_name=u'创建时间', default=datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(verbose_name=u'标签', max_length=70)
    created_time = models.DateTimeField(verbose_name=u'创建时间', default=datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=70)
    body = models.TextField(verbose_name=u'内容')
    created_time = models.DateTimeField(verbose_name=u'发布时间', default=datetime.now)
    modified_time = models.DateTimeField(verbose_name=u'修改时间', default=datetime.now)
    excerpt = models.CharField(verbose_name=u'摘要', max_length=200, blank=True)

    category = models.ForeignKey(Category, verbose_name=u'归属分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    author = models.ForeignKey(UserProfile, verbose_name=u'作者')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

