# -*- encoding:utf-8 -*-

import markdown

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View

from pure_pagination import Paginator
from pure_pagination import EmptyPage
from pure_pagination import PageNotAnInteger

from comments.forms import CommentForm
from comments.forms import ContactForm

from .models import Article
from .models import Category
from .models import ImageLib

class IndexView(View):

    def get(self, request):

        article_list = Article.objects.all().order_by('-created_time')
        try:
            page = request.GET.get('page', '1')
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_list, 5, request=request)
        article_list = p.page(page)
        return render(request, 'blog/index.html', context={'article_list': article_list})


class ArticleDetailView(View):

    def get(self, request, pk):
        article_detail = get_object_or_404(Article, pk=pk)
        article_detail.increase_click_nums()
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
        try:
            page = request.GET.get('page', '1')
        except PageNotAnInteger:
            page = 1
        p = Paginator(article_list, 5, request=request)
        article_list = p.page(page)

        return render(request,'blog/index.html', context={
                        'article_list':article_list,
                     })


class CategoryView(View):

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        article_list = Article.objects.filter(category=category).order_by('-created_time')
        try:
            page = request.GET.get('page','1')
        except PageNotAnInteger:
            page = 1
        p = Paginator(article_list, 5, request=request)
        article_list = p.page(page)

        return render(request, 'blog/index.html', context={'article_list': article_list})


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html', context={})


class ContactView(View):
    def get(self, request):
        contact_form = ContactForm()
        return render(request, 'contact.html', context={'contact_form':contact_form})


class ImageLibView(View):

    def get(self, request, year, month, image_address):
        image_join = ['images', year, month, image_address]
        address = '/'.join(image_join)
        image = get_object_or_404(ImageLib, image=address)

        return render(request, 'blog/show_image.html', context={'image': image})

