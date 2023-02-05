from .models import AccountsUser
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import transaction

@transaction.atomic
def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # auth_user save
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password1'),
                email=request.POST.get('email')
            )
            print(user)
            user_id = getattr(User.objects.get(id=user.id), "id")
            # accounts_user save
            accounts_user = AccountsUser.objects.create(
                name=request.POST.get('name'),
                birth=request.POST.get('birth'),
                phone=request.POST.get('phone'),
                address=request.POST.get('address'),
                user_id=user_id
            )
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'sign_up.html')

    return render(request, 'sign_up.html')

@transaction.atomic
def sign_in(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        userInfo = User.objects.filter(username=id)
        error_msg = '계정이 존재하지 않거나, 계정 또는 패스워드가 틀립니다.'
        if userInfo:
            user = auth.authenticate(username=id, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(request, 'user_list.html')
            else:
                return render(request, 'sign_in.html', {'errors': error_msg })
        else:
            return render(request, 'sign_in.html', {'errors': error_msg })
    else:
        return render(request, 'sign_in.html')

def user_list(request):
    if request.method == "POST":
        pass
    else:
        render(request, 'user_list.html')
