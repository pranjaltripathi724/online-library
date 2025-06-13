from django.urls import path

from .views import Author,Book,BorrowRecord


urlpatterns = [
    path('', Author.as_view(),name='Author'),
    path('Books', Book.as_view(), name='book'),
    path('Borrow', BorrowRecord.as_view(), name= 'BorrowRecord')
]