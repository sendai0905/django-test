from django.forms import ModelForm
from blog.models.article import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
