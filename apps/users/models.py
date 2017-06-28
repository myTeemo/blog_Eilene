# -*- encoding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name=u'昵称', max_length=50, default=u'')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(verbose_name=u'性别', choices=(('male', u'男'), ('female', u'女') ), default='male', max_length=7)
    address = models.CharField(verbose_name=u'地址', default=u'', max_length=50)
    mobile = models.CharField(verbose_name=u'电话', null=True, blank=True, max_length=11)
    image = models.ImageField(verbose_name=u'图片', upload_to='image/%Y/%m',default=u'image/default', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name
