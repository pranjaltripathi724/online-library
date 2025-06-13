from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Book, BorrowRecord


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Author.objects.filter(email=email).exists():
            raise ValidationError("Looks like we already have an author with this email address.")
        return email


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']


class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']

    def clean(self):
        cleaned_data = super().clean()
        borrow_date = cleaned_data.get("borrow_date")
        return_date = cleaned_data.get("return_date")

        if borrow_date and return_date and return_date < borrow_date:
            raise ValidationError("Return date can't be earlier than borrow date.")
        return cleaned_data
