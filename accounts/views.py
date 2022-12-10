from .models import AccountsUser
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # auth_user save
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email']
            )
            print(user)
            # user_id = getattr(User.objects.get(id=user.id))
            # accounts_user save
            accounts_user = AccountsUser.objects.create(
                name=request.POST['name'],
                birth=request.POST['birth'],
                phone=request.POST['phone'],
                address=request.POST['address'],
                user_id=1
            )
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'sign_up.html')

    return render(request, 'sign_up.html')