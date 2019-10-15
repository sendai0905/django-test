from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, FormView
from rest_framework import filters, viewsets

from blog.forms import ArticleForm, SearchForm
from blog.models.article import Article
from blog.models.attribute import Category, User
from blog.rfw.serializers import (ArticleSerializer, CategorySerializer,
                                  UserSerializer)


class HomeView(ListView):
    template_name = 'home.html'
    model = Article


class ArticleView(DetailView):
    template_name = 'article.html'
    model = Article


class PostArticleView(CreateView):
    template_name = 'post.html'
    form_class = ArticleForm
    success_url = reverse_lazy('blog:home')


class DeleteArticleView(DeleteView):
    template_name = 'delete.html'
    model = Article
    success_url = reverse_lazy('blog:home')


class SearchArticleView(FormView):
    template_name = 'search.html'
    form_class = SearchForm
    model = Article
    # success_url = reverse_lazy('blog:search_result')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
