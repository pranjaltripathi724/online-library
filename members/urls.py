from django.urls import path

from .admin_login_view import AdminLoginView, AdminDashboardView
from .views import (
    AuthorViews, BookViews, BorrowRecordViews,
    AuthorListView, BookListView, BorrowRecordListView, ExportExcelView
)

urlpatterns = [
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('add-author/', AuthorViews.as_view(), name='add-author'),
    path('add-book/', BookViews.as_view(), name='add-book'),
    path('add-borrow/', BorrowRecordViews.as_view(), name='add-borrow'),

    path('', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('borrow-records/', BorrowRecordListView.as_view(), name='borrow-list'),

    path('export/', ExportExcelView.as_view(), name='export-excel'),
]
