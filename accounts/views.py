from django.shortcuts import (render, redirect)
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import (RegisterForm, LoginForm, CrispyForm)


def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")


def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)