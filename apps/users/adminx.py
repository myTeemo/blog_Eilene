# -*- coding: utf-8 -*-
import xadmin
from xadmin import views


__author__ = "Eilene HE"
__date__ = '2017/6/26 09:47'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u'小木博客后台管理系统'
    site_footer = u'小木博客'
    menu_style = u'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
