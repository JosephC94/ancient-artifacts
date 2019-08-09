from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.

@login_required
def logout(request):
    """Signs a user out"""
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('index'))
    
    
def login(request):
    """Logs a user in and redirects them to the products page of artifacts"""
    if request.user.is_authenticated:
        return redirect(reverse('products'))
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
    return render(request, 'index.html', {"login_form": login_form})
    
    
def registration(request):
    """Registers a new user and redirects them to the products page upon success"""
    registration_form = UserRegistrationForm()
    return render(request, 'index.html', {'registration_form': registration_form})