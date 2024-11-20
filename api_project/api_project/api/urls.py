from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    # Retain the previous API list view (optional)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include router-generated URLs for BookViewSet
    path('', include(router.urls)),
]
