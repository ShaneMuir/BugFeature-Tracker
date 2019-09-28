from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bug
from features.models import Feature
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def register(request):
    """Lets users register to site"""
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in", 
                         extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!", 
                                 extra_tags="alert-primary")
                return redirect(reverse('index'))
            else:
                messages.error(request, 
                               "Unable to register your account at this time!",
                               extra_tags="alert-primary")

    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {
                  'registration_form': registration_form})


def login(request):
    """Logs the user in"""
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in!", 
                         extra_tags="alert-primary")
        return redirect(reverse('index'))
        
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
            password = request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!", 
                                 extra_tags="alert-primary")
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
    messages.success(request, "You have successfully been logged out!", 
                     extra_tags="alert-primary")
    return redirect(reverse('index'))
    
    
    
from graphs.graphs import bug_pie_chart, feature_pie_chart, most_upvoted_bug, most_upvoted_feature

@login_required()
def profile(request):
    """User profile page"""
    user = User.objects.get(email=request.user.email)
    bug_list = Bug.objects.filter(creator=user.id)
    feature_list = Feature.objects.filter(creator=user.id, paid=True)
    page = request.GET.get('page', 1)
    
    bug_paginator = Paginator(bug_list, 2)
    feature_paginator = Paginator(feature_list, 2)
    
    try:
        bugs = bug_paginator.page(page)
        features = feature_paginator.page(page)
    except PageNotAnInteger:
        bugs = bug_paginator.page(1)
        features = feature_paginator.page(1)
    except EmptyPage:
        bugs = bug_paginator.page(paginator.num_pages)
        features = feature_paginator.page(paginator.num_pages)
    
    
    context = {
        'profile': user,
        'bugs': bugs,
        'features': features,
        'bug_pie_chart': bug_pie_chart,
        'feature_pie_chart': feature_pie_chart,
        'most_upvoted_bug': most_upvoted_bug,
        'most_upvoted_feature': most_upvoted_feature,
    }
    
    return render(request, 'profile.html', context)
