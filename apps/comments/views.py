# -*- encoding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View

from .models import Comment
from blog.views import ArticleDetailView
from .forms import CommentForm
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
            context = {'article_detail': article_detail,
                       'comment_form': comment_form,
                       'comment_list': comment_list,
                       }
            return render(request, 'blog/detail.html',context=context)
