from django.db import models
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class BookViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    """
    queryset = Book.objects.all()  # Fetches all Book objects
    serializer_class = BookSerializer  # Specifies the serializer to use