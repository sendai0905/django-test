from django.urls import path
from blog.views import HomeView, ArticleView, PostArticleView, DeleteArticleView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
    path('post/', PostArticleView.as_view(), name='post'),
    path('delete/<int:pk>', DeleteArticleView.as_view(), name='delete'),
]
