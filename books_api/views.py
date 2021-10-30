import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import viewsets

from books_api.models import Book
from books_api.serializers import BookSerializer
from books_api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["name", "writer", "genre", "price", "synopsis", "release"]
    search_fields = ["name", "writer", "synopsis"]
