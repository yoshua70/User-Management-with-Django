from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            messages.success(request, ("Echec de l'authentification."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def dashboard(request):
    return render(request, 'members/index.html', {})
