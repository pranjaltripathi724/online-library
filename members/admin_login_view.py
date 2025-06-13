from django.views import View
from django.shortcuts import render ,redirect

# credentials
ADMIN_USERNAME = 'pranjal'
ADMIN_PASSWORD = '123456'

class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('admin-dashboard')  
        return render(request, 'admin_login.html', {'error': 'Invalid credentials'})


class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('is_admin'):
            return redirect('admin-login')
        return super().dispatch(request, *args, **kwargs)

class AdminDashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'admin_dashboard.html')