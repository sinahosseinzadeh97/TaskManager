from django.shortcuts import render, get_object_or_404, redirect
from ..models import Author


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'Library/authors/author_list.html', {'authors': authors})


def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        biography = request.POST.get('biography')
        birth_date = request.POST.get('birth_date')  # Fixed typo from 'birh_date' to 'birth_date'

        # Create and save the new author instance
        Author.objects.create(author_name=author_name, biography=biography, birth_date=birth_date)

        return redirect('author_list')
    return render(request, 'Library/authors/add_author.html')


def edit_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        # Update the author with new data from the form
        author.author_name = request.POST.get('author_name')
        author.biography = request.POST.get('biography')
        author.birth_date = request.POST.get('birth_date')

        author.save()  # Save the updated author instance
        return redirect('author_list')
    return render(request, 'Library/authors/edit_author.html', {'author': author})
