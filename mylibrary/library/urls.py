from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CoverViewSet
from .views import AuthorDetailView, BookCreateView, BookDetailView

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'covers', CoverViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]

