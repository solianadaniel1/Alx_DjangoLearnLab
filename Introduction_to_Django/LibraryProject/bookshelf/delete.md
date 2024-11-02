# Delete Operation

First, ensure the Book model is imported:

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()