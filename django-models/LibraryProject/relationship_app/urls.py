from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import LoginView
from .views import LogoutView
from .import views 
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from .views import add_book 
from .views import edit_book 
from .views import delete_book


urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("admin-area/", admin_view, name="admin_view"),
    path("librarian-area/", librarian_view, name="librarian_view"),
    path("member-area/", member_view, name="member_view"),
    path("books/add/", add_book, name="add_book"),
    path("books/<int:pk>/edit/", edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", delete_book, name="delete_book"),
    
]