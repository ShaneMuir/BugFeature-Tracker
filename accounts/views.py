from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bug
from features.models import Feature


# Create your views here.
def register(request):
    """Lets users register to site"""
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in", extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!", extra_tags="alert-primary")
                return redirect(reverse('index'))
            else:
                messages.error(request, 
                "Unable to register your account at this time!")
                
            
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html',
    {'registration_form': registration_form})


def login(request):
    """Logs the user in"""
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in!", extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
            password = request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!", extra_tags="alert-primary")
                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {"login_form": login_form})


@login_required()
def logout(request):
    """Log out the user"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!", extra_tags="alert-primary")
    return redirect(reverse('index'))


@login_required()
def profile(request):
    """User profile page"""
    user = User.objects.get(email=request.user.email)
    bugs = Bug.objects.filter(creator=user.id)
    features = Feature.objects.filter(creator=user.id)
    
    context = {
        'profile': user,
        'bugs': bugs,
        'features': features,
    }
    
    return render(request, 'profile.html', context)