from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # Import the Book model lazily to avoid circular imports
        from api.models import Book
        model = Book
        fields = '__all__'
