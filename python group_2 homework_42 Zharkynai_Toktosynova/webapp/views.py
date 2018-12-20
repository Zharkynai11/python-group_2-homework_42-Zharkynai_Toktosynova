from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View, RedirectView
from webapp.models import *
from django.utils import timezone


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['articles'] = Article.objects.all()
        return context

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['comments'] = Comment.objects.all()
        context['marks'] = Mark.objects.all()
        return context

class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'

#
# class MarkListView(ListView):
#     model = Mark
#     template_name = 'mark_list.html'
#
#
# class MarkDetailView(DetailView):
#     model = Mark
#     template_name = 'mark_detail.html'
# Create your views here.
