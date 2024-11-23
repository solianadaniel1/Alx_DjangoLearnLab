from rest_framework.generics import ListAPIView  
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

# Define the BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Query all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer for this view
