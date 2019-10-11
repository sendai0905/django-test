from rest_framework import routers
from blog.views import UserViewSet, CategoryViewSet, ArticleViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'article', ArticleViewSet)
