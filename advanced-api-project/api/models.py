from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can be associated with multiple books.
    This establishes a one-to-many relationship where one Author can have many Books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a published book.
    Each book is linked to exactly one Author via a foreign key relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables author.books access
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
