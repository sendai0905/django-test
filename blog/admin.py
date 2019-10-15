# -*- coding: utf-8 -*-
from django.contrib import admin

from .models.attribute import User, Category
from .models.article import Article


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'detail',
        'pub_date',
        'author',
        'category',
    )
    list_filter = ('pub_date', 'author', 'category')


# @admin.register(Unko)
# class UnkoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text')
