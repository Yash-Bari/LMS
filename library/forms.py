from django import forms
from .models import Book, IssuedBook

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'genre', 'published_date', 'description']


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['book', 'borrower', 'issue_date', 'return_date']  # Include 'return_date' field
