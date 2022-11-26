from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('/')

            else:
                messages.error(request,
                               f"Please enter correct username and password. Note that both the fields are "
                               f"case-sensitive.")
                return redirect('login_user')

        else:
            return render(request, 'login.html', {})


def logout_user(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')
