# Retrieve Operation

This document outlines the steps taken to retrieve a Book instance and display its attributes.

## Command

1. **Retrieve the Book instance**:
   To retrieve the book titled “1984”, use the following command:

   ```python
   retrieved_book = Book.objects.get(title="1984")

2. **Print retrived book**:
   To print the book , use the following command:

   ```python
    print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

# output
1984 George Orwell 1949