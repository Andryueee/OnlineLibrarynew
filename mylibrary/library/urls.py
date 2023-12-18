# library/urls.py

from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CoverViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'covers', CoverViewSet)

urlpatterns = router.urls
