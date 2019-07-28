from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Bug


# Create your views here.

def show_all_bugs(request):
    """
    View to show all our bugs on
    one page
    """
    bugs = Bug.objects.filter(created_date__lte=timezone.now()
                             ).order_by('upvotes')
    
    context = {
        'bugs': bugs
    }
    
    return render(request, 'bugs.html', context)