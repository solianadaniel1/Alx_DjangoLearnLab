from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden

# View for creating a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        publication_date = request.POST.get('publication_date')
        
        book = Book.objects.create(
            title=title,
            author=author,
            description=description,
            publication_date=publication_date
        )
        return render(request, 'book_detail.html', {'book': book})
    return render(request, 'create_book.html')

# View for editing a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.publication_date = request.POST.get('publication_date')
        book.save()
        return render(request, 'book_detail.html', {'book': book})
    return render(request, 'edit_book.html', {'book': book})

# View for deleting a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'book_list.html')

# View for viewing a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
