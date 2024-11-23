from rest_framework import generics
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import your serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Define the BookList view
class BookList(generics.ListAPIView):  # Ensure the class extends ListAPIView
    queryset = Book.objects.all()  # Query all Book instances
    serializer_class = BookSerializer  # Specify the serializer for this view

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
    permission_classes = [IsAuthenticated]  # Default to IsAuthenticated for all users
    
    def get_permissions(self):
        """
        Override to allow admins to delete books
        """
        if self.action == 'destroy':  # Allow only admin to delete
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]