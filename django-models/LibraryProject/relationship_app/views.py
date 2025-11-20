from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
#function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


#class-based detail view for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'