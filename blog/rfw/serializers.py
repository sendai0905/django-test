from rest_framework import serializers
from blog.models import article, attribute


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = attribute.User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = attribute.Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article.Article
        fields = '__all__'
