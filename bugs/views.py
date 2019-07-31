from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Bug, BugComment, upVotes
from .forms import BugCommentForm

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
            bug_comment = BugComment.objects.create(bug=bug, creator=request.user, comment=comment)
            bug_comment.save()
            return redirect(single_bug_view, bug.pk)
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
        messages.success(request, "Bug upvoted", extra_tags="alert-success")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Sorry {0} you have already upvoted {1}!'.format(request.user, bug.title), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))
        