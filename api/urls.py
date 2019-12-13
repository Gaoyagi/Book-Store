from django.urls import path

from api.views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetail.as_view(), name='books_detail')
]