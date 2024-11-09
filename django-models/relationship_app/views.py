from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render, get_object_or_404, redirect
from relationship_app.models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from .form import BookForm  # Assuming you have a form for handling Book
from django.contrib.auth.decorators import permission_required

# View to add a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book
            return redirect('book_list')  # Redirect to book list after saving
    else:
        form = BookForm()  # Empty form for GET requests
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Update the existing book
            return redirect('book_list')  # Redirect to book list after saving
    else:
        form = BookForm(instance=book)  # Populate the form with the existing book data
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()  # Delete the book
        return redirect('book_list')  # Redirect to book list after deleting
    return render(request, 'relationship_app/delete_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to a list of books or another page
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})

def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Custom view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role check helper functions
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Function to check if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view that only accessible by users with 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    # Render the template for the librarian view
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')