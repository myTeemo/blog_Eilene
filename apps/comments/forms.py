# -*- coding: utf-8 -*-
from django import forms

from .models import Comment

__author__ = "Eilene HE"
__date__ = '2017/6/26 17:47'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']


