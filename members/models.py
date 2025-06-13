from django.db import models
from django.core.validators import validate_email

class Author(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validate_email])
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    user_name = models.CharField(max_length=255)
    book =  models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date =  models.DateField()
    return_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.user_name
