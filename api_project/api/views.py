from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# Existing ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# NEW: Full CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list(), retrieve(), create(), update(), partial_update(), destroy()
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
