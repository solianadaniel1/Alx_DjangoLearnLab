from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

# List and Create View (GET for all books, POST for adding a new book)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read access for all users
    
    def perform_create(self, serializer):
        # Ensure the publication year is not in the future
        if serializer.validated_data['publication_year'] > now().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# Detail, Update, and Delete View (GET, PUT, DELETE for specific book)
class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated users for modifications
    
    def perform_update(self, serializer):
        # Ensure the publication year is not in the future
        if serializer.validated_data.get('publication_year') and serializer.validated_data['publication_year'] > now().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()
