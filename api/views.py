from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from books.models import Book
from api.serializers import BookSerializer


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer