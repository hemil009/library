from django.shortcuts import render, redirect
from .models import Book
from . import forms
from django.db.models import Q



def book_list(request):
    if request.method == 'POST':
        genre = request.POST.get('genre')
        language = request.POST.get('language')
        bookobj = Book.objects.filter(
            Q(genre__icontains=genre), Q(language__icontains=language))
        return render(request, "books/book_list.html", {'books': bookobj})
    else:
        books = Book.objects.all()
        return render(request, "books/book_list.html", {"books": books})

def book_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('books:list')
    else:
        form = forms.CreateArticle()
    return render(request, "books/book_create.html", {"form": form})


