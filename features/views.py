from django.shortcuts import render, get_object_or_404
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
    


def single_feature_view(request, pk):
    """
    Route to view a single feature on
    one page
    """
    feature = get_object_or_404(Feature, pk=pk)
    
    feature.views += 1
    feature.save()
    
    
            
    context = {
        'feature' : feature,
    }
    return render(request, 'single_feature.html', context)