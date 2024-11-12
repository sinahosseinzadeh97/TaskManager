# This should be in Library/views/__init__.py, NOT in Library/__init__.py
from .author_views import author_list, add_author, edit_author
from .book_views import book_list, add_book, edit_book

from django.shortcuts import render

def library_home(request):
    return render(request, 'Library/home.html')
