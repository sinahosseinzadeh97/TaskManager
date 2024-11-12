from django.shortcuts import render, get_object_or_404, redirect
from ..models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Library/books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        publication_date = request.POST.get('publication_date')
        author_id = request.POST.get('author')

        # Fetch the author
        author = get_object_or_404(Author, id=author_id)

        # Create and save the new book
        Book.objects.create(book_title=book_title, publication_date=publication_date, author=author)
        return redirect('book_list')

    # Fetch all authors to display in the dropdown
    authors = Author.objects.all()
    return render(request, 'Library/books/add_book.html', {'authors': authors})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.book_title = request.POST.get('book_title')
        book.publication_date = request.POST.get('publication_date')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('book_list')
    return render(request, 'Library/books/edit_book.html', {'book': book})
