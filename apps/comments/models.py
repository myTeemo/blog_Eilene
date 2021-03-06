# -*- encoding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from blog.models import Article


class Comment(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=30)
    email = models.EmailField(verbose_name=u'电子邮箱', max_length=255)
    url = models.URLField(verbose_name=u'站点')
    text = models.TextField(verbose_name=u'评论内容')
    created_time = models.DateTimeField(verbose_name=u'评论时间', default=datetime.now)

    article = models.ForeignKey(Article, verbose_name=u'所属文章')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text[:20]


class Contact(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=30)
    email = models.EmailField(verbose_name=u'电子邮件', max_length=255)
    subject = models.CharField(verbose_name=u'主题', max_length=20)
    text = models.TextField(verbose_name=u'留言信息')

    created_time = models.DateTimeField(verbose_name=u'留言时间', default=datetime.now)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = verbose_name

