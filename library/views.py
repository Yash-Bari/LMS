from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Book, IssuedBook
from .forms import BookForm, IssueBookForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    template_name = 'library/login.html'  # Specify the template name for the login form
    success_url = reverse_lazy('home')  # Redirect to the home page after successful login

def custom_logout(request):
    logout(request)
    return redirect('login') 

@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful form submission
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})
@login_required
@user_passes_test(lambda u: u.is_staff)
def view_issued_books(request):
    issued_books = IssuedBook.objects.all()
    return render(request, 'library/view_issued_books.html', {'issued_books': issued_books})

@login_required
@user_passes_test(lambda u: u.is_staff)
def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page or a confirmation page
    else:
        form = IssueBookForm()
    # Fetch all books and users to populate select dropdowns
    books = Book.objects.all()
    users = User.objects.all()
    return render(request, 'library/issue_book.html', {'form': form, 'books': books, 'users': users})