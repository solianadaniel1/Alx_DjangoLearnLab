from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(ModelViewSet):
    """
    ViewSet for handling all CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer to handle serialization
    permission_classes = [IsAuthenticated]  # Require authentication for all users
    
    def get_permissions(self):
        if self.action == 'destroy':  # Only admins can delete
            return [IsAdminUser()]
        return super().get_permissions()