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

    
def knights_sword(request):
    """Directs user to info page about the knights Templar"""
    return render(request, 'knights_sword.html')
    
def holy_grail(request):
    """Directs user to info page about the Holy Grail"""
    return render(request, 'holy_grail.html')
    
def tutankhamun(request):
    """Directs user to info page about the Mask of Tutankhmun"""
    return render(request, 'tutankhamun.html')

def sandals(request):
    """Directs user to info page about the Sandals of Jesus"""
    return render(request, 'jesus_sandals.html')
    
def excalibur(request):
    """Directs user to info page about the Excalibur"""
    return render(request, 'excalibur.html')
    
def belt(request):
    """Directs user to info page about the Belt of Aphrodite"""
    return render(request, 'belt.html')
    
def hammer(request):
    """Directs user to info page about Mjöllnir"""
    return render(request, 'hammer.html')
    
def lamp(request):
    """Directs user to info page about the Geni's Lamp"""
    return render(request, 'lamp.html')