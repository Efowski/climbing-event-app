from django.shortcuts import render, redirect

from .forms import RegistrationMembersForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from event.models import User, Event
from event.form import UserForm
from django.contrib import messages


def activate_email(request, user, to_email):
    messages.success(request, f'Hey <b>{user} please check Your {to_email} and clik to active Your account on the ClimbEvents App ')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationMembersForm(request.POST)
        if form.is_valid:
            
           form.save()
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
             
           user = authenticate(username=username, password=password)
           login(request, user)
           messages.success(request,f"{{user.username}} account was a create!")
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


@login_required(login_url='login')
def user_profile(request, id):
    user = User.objects.get(id=id)
    user_form = UserForm(instance=user)

    events = Event.objects.filter(participants=request.user)
    
    return render(request, 'user_profile.html', {'user': user, 'user_form': user_form, 'events': events,   })

@login_required
def update_profile(request, id):
    user = User.objects.get(id=id)
    user_form = UserForm(request.POST or None, instance=request.user)

    if request.method == 'POST':
       if  user_form.is_valid():

            user_form.save()
            messages.success(request, "Profile was updated succesfully")
            return redirect('home')



    return render(request, 'update_profile.html', {'user': user, 'user_form': user_form,})


@login_required
def delete_user_account(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success('Your account was delete')
    return render(request, 'home')


