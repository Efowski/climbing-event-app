from django.shortcuts import render, redirect

from .forms import RegistrationMembersForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = RegistrationMembersForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Registration was success")
            return redirect('home')
        
    else:
        form = RegistrationMembersForm()

    return render(request, 'register_user.html', {'form': form, })


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            
            return redirect('home')
        else: 
            messages.success(request, "Invalid login or password")
            return redirect ('login-user')

    return render(request, 'login_user.html', )


def logout_user(request):
    logout(request)
    messages.success(request, "You logout is success")
    return redirect('home')


def user_profile(request, pk):
    pass
