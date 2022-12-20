from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform_password = request.POST['conform_password']

        if password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('/')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('/')
                else:
                    user = User.objects.create_user(
                        first_name=firstname,  email=email, username=username, password=password)
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in.')
                    # return redirect('/')
                    user.save()
                    messages.success(
                        request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Your are now logged in')
            return redirect('homes')
        else:
            messages.error(request, 'Invalid Login credentials')
            return redirect('login')

    return render(request, 'pages/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('login')
    return redirect('login')
