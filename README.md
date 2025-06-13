Install required packages
1.pip install Django
2. pip install django openpyxl

Run database migrations
1. python manage.py makemigrations
2. python manage.py migrate

Create a superuser
1. python manage.py createsuperuser

Start the development server
1. python manage.py runserver

Access the application
1. Open your browser and go to http://127.0.0.1:8000/
2. Admin login: http://127.0.0.1:8000/admin-login/
Username = pranjal
password = 123456

Main Features
1. Author Management

Navigate to "Add Author" to create new author profiles
View all authors in the authors list with pagination
Each author has name, email (unique), and biography fields

2. Book Management

Add new books with title, genre, publication date, and author assignment
Browse all books in the catalog
Books are linked to their respective authors

3. Borrow Record Management

Create borrowing records with user name, book selection, and dates
Track both borrow and return dates
View all borrowing history with pagination

4. Data Export

Export complete library data to Excel format
Includes separate sheets for Authors, Books, and Borrow Records
Accessible through the admin dashboard


API Endpoints
URL                        View                      Description              Admin Required
/                     AuthorListView              List all authors              No
/books/                BookListView              List all books               No
/borrow-records/      BorrowRecord ListView      List borrow records          No
/admin-login/        AdminLoginView              Admin login page              No
/admin-dashboard/      AdminDashboard            ViewAdmin dashboard            Yes
/add-author/          AuthorViews                Add new author                Yes
/add-book/            BookViews                  Add new book                  Yes
/add-borrow/        BorrowRecord              ViewsAdd borrow record          Yes
/export/            ExportExcel                ViewExport to Excel            Yes
