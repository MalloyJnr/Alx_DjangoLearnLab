import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    """
    Defines filtering options for the Book model.
    """

    title = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter()
    author = django_filters.NumberFilter(field_name='author__id')

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
