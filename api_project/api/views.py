from rest_framework import generics
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import your serializer

# Define the BookList view
class BookList(generics.ListAPIView):  # Ensure the class extends ListAPIView
    queryset = Book.objects.all()  # Query all Book instances
    serializer_class = BookSerializer  # Specify the serializer for this view
