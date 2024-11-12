from django.urls import path
from .views import library_home, author_list, add_author, edit_author, book_list, add_book, edit_book

urlpatterns = [
    path('', library_home, name='library_home'),  # Root URL for /library/
    path('authors/', author_list, name='author_list'),
    path('authors/add/', add_author, name='add_author'),
    path('authors/edit/<int:pk>/', edit_author, name='edit_author'),
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
]
