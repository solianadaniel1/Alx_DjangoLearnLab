# Delete Operation

This document outlines the steps taken to delete the Book instance previously created and confirm its deletion.

## Command

1. **Retrieve the book instance to delete**:
    To delete the book titled “Nineteen Eighty-Four”, first retrieve it:

    ```python
    retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
    ```

2. **Delete the retrieved book**:
    Once you have the instance, you can delete it:

    ```python
    retrieved_book.delete()
    ```

3. **Confirm Deletion**:
    To confirm that the book has been deleted, retrieve all books:

    ```python
    books = Book.objects.all()
    print(books)
    ```

## Output

The expected output is:

