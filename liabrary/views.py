from django.shortcuts import render
from .models import Book, Author



def index(req):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors,
    }
    return render(req, 'liabrary/index.html', context)



