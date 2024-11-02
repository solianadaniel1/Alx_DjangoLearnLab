# Create Operation

This document outlines the steps taken to create a new Book instance and confirm its creation.

## Command

1. **Create a Book instance**:
   To create a book titled “1984” by George Orwell, published in 1949, use the following command:

   ```python
   book = Book(title="1984", author="George Orwell", publication_year=1949)

2. **Save a Book**:
   Save book titled “1984” by George Orwell, published in 1949, use the following command:

   ```python
   book.save()

3. **Confirming the creation of the book**:
    Confirming the creation of the book, use the following command:

   ```python
    Book.objects.all()

## Output

The expected output is: 1984



