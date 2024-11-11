# Update Operation

This document outlines the steps taken to update the title of a Book instance from “1984” to “Nineteen Eighty-Four” and save the changes.

## Command

1. **Retrieve the Book instance**:
   To retrieve the book titled “1984”, use the following command:

   ```python
   retrieved_book = Book.objects.get(title="1984")

2. **Update the book title**:
   Update the book title , use the following command:

   ```python
    retrieved_book.title = "Nineteen Eighty-Four"

3. **Save the book title**:
   Update the book title , use the following command:

   ```python
    retrieved_book.save()

3. **Retrieve the book title**:
   Update the book title , use the following command:

   ```python
    updated_book = Book.objects.get(title="Nineteen Eighty-Four")

3. **Print the book**:
   Update the book title , use the following command:

   ```python
    print(updated_book.title)

# output
Nineteen Eighty-Four