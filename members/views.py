from email import message
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from pydantic import ValidationError, validate_email
from . import models
from .models import Book, Author
# from Task.members import models
# Create your views here.



class Author(View):
    def get(self, request):
        return render(request, 'Author.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        # try:
        #     validate_email(email)
        #     if not email.endswith('@gmail.com'):
        #         raise ValidationError("Only Gmail addresses allowed.")
        # except ValidationError as e:
        #     return render(request, 'Author.html', {'error': str(e)})
        # try:
        #     data=models.Author(name=name, email=email, bio=bio)
        #     data.save()
        #     return redirect('Author')
        # except IntegrityError:
        #     return render(request, 'Author.html', {'error': 'Email already exists.'})
        
        if not validate_email(email):
            return render(request, 'Author.html', {'error': 'Invalid Email Formate'})

        try:
            Author.objects.get(email=email)
            return render(request, 'Author.html', {'error': 'Email already exists.'})
        except IntegrityError:
            Author.objects.create(name=name, email=email, bio=bio)
            return render(request, 'Author.html', {'success': 'Author added successfully'})


class Book(View):
    def get(self, request):
        authors = models.Author.objects.all()
        return render(request, 'Book.html', {'authors': authors})

    def post(self, request):
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        published_date = request.POST.get('published_date')
        author_id = request.POST.get('author_id')
        author = models.Author.objects.get(id=author_id)
        book = models.Book(title=title, genre=genre, published_date=published_date, author=author)
        book.save()
        authors = models.Author.objects.all()
        return render(request, 'Book.html', {'authors': authors, 'message': "Data Added Successfully"})
    



class BorrowRecord(View):
    def get(self, request):
        books = models.Book.objects.all()
        return render(request, 'BorrowRecord.html', {'books': books})

    def post(self, request):
        user_name = request.POST.get('user_name')
        borrow_date = request.POST.get('borrow_date')
        return_date = request.POST.get('return_date')
        book_id = request.POST.get('book_id')
        book = models.Book.objects.get(id=book_id)
        BorrowRecord = models.BorrowRecord(user_name=user_name, borrow_date=borrow_date, return_date=return_date, book=book)
        BorrowRecord.save()
        books = models.Book.objects.all()
        return render(request, 'BorrowRecord.html', {'books': books, 'message': "Data Added Successfully"})    