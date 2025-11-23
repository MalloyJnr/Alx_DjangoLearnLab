from bookshelf.models import Book
>>> 
>>> b = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )
>>> 
>>> b
<Book: 1984>
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>
>>> b = Book.objects.get(title="1984")
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
>>> b
<Book: Nineteen Eighty-Four>
>>> b.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
>>>