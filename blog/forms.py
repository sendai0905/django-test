from django import forms

from blog.models.article import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', max_length=100, required=True)
