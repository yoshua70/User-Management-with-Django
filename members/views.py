from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Account
from django.contrib.auth.models import User


def register_user_by_admin(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            account = Account(
                user=user, db=form.cleaned_data["database_revue"])
            account.save()
            messages.success(request, "Utilisateur ajouté avec succès !")

            return redirect('dashboard')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_by_admin.html', {'form': form})


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
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)

    return redirect('login')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users = User.objects.filter(is_superuser=0)

    return render(request, 'members/index.html', {"users": users})


def delete_user(request, id):

    User.objects.get(username=id).delete()
    messages.success(request, ("Utilisateur supprimé."))
    return redirect('dashboard')
