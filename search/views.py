from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature

# Create your views here.
def search(request):
    bugs = Bug.objects.filter(title__icontains=request.GET['q'])
    features = Feature.objects.filter(title__icontains=request.GET['q']).exclude(paid=False)
    
    context = {
        'bugs': bugs,
        'features': features,
    }
    return render(request, "search.html", context)