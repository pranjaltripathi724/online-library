from django.db import models
from django.core.validators import validate_email

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validate_email])
    bio = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BorrowRecord(models.Model):
    user_name = models.CharField(max_length=255)
    book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date =  models.DateField()
    return_date =  models.DateField(blank=True)  