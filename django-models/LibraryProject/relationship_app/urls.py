from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import LoginView
from .views import LogoutView
from .import views 

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_view, name="register"),
    
]