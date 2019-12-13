from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from books.models import Book
from books.forms import BookCreateForm

class BookListView(ListView):
    """ Renders a list of all Pages. """
    model = Book

    def get(self, request):
        """ GET a list of Pages. """
        bookList = self.get_queryset().all()
        return render(request, 'list.html', {
          'bookList': bookList
        })

class BookDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Book

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        bookQuery = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'bookQuery': bookQuery
        })

class BookCreateView(CreateView):
    model = Book

    def get(self, request, *args, **kwargs):
        context = {'form': BookCreateForm()}
        return render(request, 'pages/create.html', context)

    def post(self, request, *args, **kwargs):
      form = BookCreateForm(request.POST)
      pages = self.get_queryset().all()
      if form.is_valid():
          page = form.save()
          page.save()
          return render(request, 'page.html', {
            'page': page
          })
      return render(request, 'list.html', {
        'pages': pages
      })