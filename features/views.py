from django.shortcuts import render
from .models import Feature
from django.utils import timezone

# Create your views here.
def show_all_features(request):
    """
    View to show all our bugs on
    one page
    """
    features = Feature.objects.filter(created_date__lte=timezone.now())
    
    context = {
        'features': features
    }
    return render(request, 'features.html', context)