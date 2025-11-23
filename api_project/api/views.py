from rest_framework import generics
from .models import book
from .serializer import BookSerializer

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer


    