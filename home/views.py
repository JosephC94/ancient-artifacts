from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm

# Create your views here.

def index(request):
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have been logged in")
                return redirect(reverse('products'))
            else:
                login_form.add_error(None, 'Please try again')
                messages.success(request, "Your username or password is incorrect")
            
    else:
        login_form = UserLoginForm()
    return render(request, 'index.html', {'login_form': login_form})

    
