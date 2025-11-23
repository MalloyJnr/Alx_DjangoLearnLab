from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing list endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # New CRUD endpoints via the router
    path('', include(router.urls)),
]
