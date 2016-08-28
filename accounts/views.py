from django.shortcuts import render


def register_view(request):
    return render(request, 'accounts/register.html', {'title': 'Registration'})


def login_view(request):
    return render(request, 'accounts/login.html', {'title': 'Login'})


def logout_view(request):
    return render(request, 'accounts/logout.html', {'title': 'Logout'})
