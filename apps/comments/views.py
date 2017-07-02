# -*- encoding:utf-8 -*-

import markdown

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View

from .forms import CommentForm
from .forms import ContactForm
from blog.models import Article


class PostCommentView(View):

    def get(self, request):
        pass

    def post(self, request, pk):
        article_detail = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article_detail
            comment.save()
            return redirect('blog:article_detail', pk=pk)
        else:
            comment_list = article_detail.comment_set.all()
            article_detail.body = markdown.markdown(article_detail.body,
                                                    extensions=[
                                                        'markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc',
                                                    ])
            context = {'article_detail': article_detail,
                       'comment_form': comment_form,
                       'comment_list': comment_list,
                       }
            return render(request, 'blog/detail.html',context=context)


class PostContactView(View):
    def get(self, request):
        pass

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect('blog:index')
        else:
            context = {
                'contact_form': contact_form,
            }
            return render(request, 'contact.html', context=context)

