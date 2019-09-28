from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Bug, BugComment, upVotes
from .forms import BugCommentForm, BugCreationForm


# Create your views here.
def show_all_bugs(request):
    """
    View to show all our bugs on
    one page
    """
    bugs = Bug.objects.filter(created_date__lte=timezone.now())
    
    context = {
        'bugs': bugs
    }
    return render(request, 'bugs.html', context)


def single_bug_view(request, pk):
    """
    Route to view a single bug on
    one page
    """
    bug = get_object_or_404(Bug, pk=pk)
    
    if request.method == 'POST':
        bug_comment_form = BugCommentForm(request.POST or None)
        if bug_comment_form.is_valid():
            comment = request.POST.get('comment')
            bug_comment = BugComment.objects.create(bug=bug, creator=request.user,
                                                    comment=comment)
            bug_comment.save()
            messages.success(request, 'Thanks {} your comment has posted'
                             .format(request.user), extra_tags="alert-primary")
            return redirect(reverse('single_bug_view', kwargs={'pk': pk}))
    else:
        bug_comment_form = BugCommentForm()
        bug.views += 1
        bug.save()
    
    comments = BugComment.objects.filter(bug=bug)
    
    bug_comment_form = BugCommentForm()
            
    context = {
        'bug' : bug,
        'bug_comment_form': bug_comment_form,
        'comments': comments,
    }
    return render(request, 'single_bug.html', context)
    

@login_required
def upvote_bug(request, bug_id):
    """
    Route to allow users to upvote bugs
    
    """
    bug = Bug.objects.get(pk=bug_id)
    check_user_voted = upVotes.objects.filter(upvote_user=request.user, bug=bug)
    if not check_user_voted:
        upvote = upVotes(upvote_user=request.user, bug=bug)
        upvote.save()
        bug.bug_upvotes += 1
        bug.save()
        messages.success(request, "Bug upvoted", extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Sorry {0} you have already upvoted {1}!'.format(
                       request.user, bug.title), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def create_a_bug(request):
    """
    Route to allow users to be able to create a bug
    via the BugCreationForm
    """
    if request.method == "POST":
        form = BugCreationForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.creator = request.user
            bug = form.save()
            messages.success(request, 'Thank you {0}, your bug has been created!'
                             .format(request.user), extra_tags="alert-primary")
            return redirect(reverse('show_all_bugs'))
    else:
        form = BugCreationForm()
        
    context = {
        'form' : form
    }
    return render(request, 'create_bug.html', context)


@login_required
def edit_a_bug(request, pk):
    """
    Route to allow users to edit their bugs
    """
    bug = get_object_or_404(Bug, pk=pk)
    
    if request.method == "POST":
        form = BugCreationForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.creator = request.user
            bug.save()
            messages.success(request, "Thanks {0}, {1} has been updated."
                             .format(request.user, bug.title),
                             extra_tags="alert-primary")
            return redirect(reverse('profile'))
    
    else:
        form = BugCreationForm(instance=bug)
        
    context = {
        'form': form,
    }
    return render(request, 'edit_bug.html', context)
 
   
@login_required
def delete_a_bug(request, pk):
    """
    Route to allow users to delete their bugs
    """
    bug = get_object_or_404(Bug, pk=pk)
    
    if request.method == "POST":
        bug.delete()
        messages.success(request, '{} your bug has been deleted!'
                         .format(request.user), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 
                       '{} unfortunatley at this time your bug cannot be deleted.'
                       .format(request.user), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))
