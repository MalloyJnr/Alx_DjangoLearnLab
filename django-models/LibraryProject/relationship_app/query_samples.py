# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books


# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # from OneToOne relationship


# Example usage (if running inside Django shell or script)
if __name__ == "__main__":
    print("Books by Author:")
    for book in get_books_by_author("John Doe"):
        print(book)

    print("\nBooks in Library:")
    for book in get_books_in_library("Central Library"):
        print(book)

    print("\nLibrarian for Library:")
    print(get_librarian_for_library("Central Library"))





# def sample_queries():
#     # Create an author
#     author = Author.objects.create(name="J.K. Rowling")

#     # Create a book
#     book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author)

#     # Create a library
#     library = Library.objects.create(name="Central Library")
#     library.books.add(book)

#     # Create a librarian
#     librarian = Librarian.objects.create(name="Alice", library=library)

#     # Query examples
#     all_authors = Author.objects.all()
#     all_books = Book.objects.filter(author__name="J.K. Rowling")
#     librarian_library = Librarian.objects.get(name="Alice").library

#     return {
#         "all_authors": all_authors,
#         "all_books": all_books,
#         "librarian_library": librarian_library,
#     }