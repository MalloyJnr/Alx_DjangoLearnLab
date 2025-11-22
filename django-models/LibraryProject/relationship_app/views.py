from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

# Create your views here.
#function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


#class-based detail view for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class LoginUserView(LoginView):
    template_name = 'relationship_app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('list_books')

def get_success_url(self):
    return self.success_url

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in after registration
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})
