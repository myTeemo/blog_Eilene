# -*- encoding:utf-8 -*-

import markdown

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.base import View

from comments.forms import CommentForm

from .models import Article
from .models import Category


class IndexView(View):

    def get(self, request):
        article_list = Article.objects.all().order_by('-created_time')
        return render(request, 'blog/index.html', context={'article_list': article_list})


class ArticleDetailView(View):

    def get(self, request, pk):
        article_detail = get_object_or_404(Article, pk=pk)
        article_detail.body = markdown.markdown(article_detail.body,
                                                extensions=[
                                                    'markdown.extensions.extra',
                                                    'markdown.extensions.codehilite',
                                                    'markdown.extensions.toc',
                                                ])
        comment_form = CommentForm()
        comment_list = article_detail.comment_set.all()
        context = {
            'article_detail': article_detail,
            'comment_form': comment_form,
            'comment_list': comment_list,
        }
        return render(request, 'blog/detail.html', context=context)


class ArchivesView(View):

    def get(self, request, year, month):
        article_list = Article.objects.filter(created_time__year=year,
                                              created_time__month=month).order_by('-created_time')
        return render(request,'blog/index.html', context={
                        'article_list':article_list,
                     })


class CategoryView(View):

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        article_list = Article.objects.filter(category=category).order_by('-created_time')
        return  render(request, 'blog/index.html', context={'article_list': article_list})

