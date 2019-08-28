from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature

# Create your views here.
def search(request):
    bugs = Bug.objects.filter(title__icontains=request.GET['q'])
    features = Feature.objects.filter(title__icontains=request.GET['q'], paid=True)
    bug_count = bugs.count()
    feature_count = features.count()
    
    context = {
        'bugs': bugs,
        'features': features,
        'bug_count': bug_count,
        'feature_count': feature_count,
    }
    return render(request, "search.html", context)