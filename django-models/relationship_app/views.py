from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library

def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'templates/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/library_detail.html'
    context_object_name = 'library'