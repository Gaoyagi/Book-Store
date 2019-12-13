from django import forms
from books.models import Book


class BookCreateForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Book
        fields = "__all__"