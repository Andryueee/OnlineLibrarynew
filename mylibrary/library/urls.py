# library/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CoverViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'covers', CoverViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # другие URL-адреса, если есть
]
