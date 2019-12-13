from django.urls import path
from books.views import BookListView, BookDetailView, BookCreateView


urlpatterns = [
    path('', BookListView.as_view(), name='book-list-page'),
    path('create/', BookCreateView.as_view(), name='book-new-page'),
    path('<str:slug>/', BookDetailView.as_view(), name='book-details-page'),
]
