from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets, filters
from blog.models.attribute import User, Category
from blog.models.article import Article
from blog.forms import ArticleForm
from blog.rfw.serializers import UserSerializer, CategorySerializer, ArticleSerializer


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
