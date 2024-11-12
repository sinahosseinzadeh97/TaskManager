from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=255)  # Name of Author
    biography = models.CharField(max_length=255)    # Biography of Author
    birth_date = models.DateField(null=True, blank=True)  # Birth date of Author

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_title = models.CharField(max_length=255)  # Title of Book
    publication_date = models.DateField()  # Publication date
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to Author

    def __str__(self):
        return self.book_title
