from django.shortcuts import render

# Create your views here.
def index(request):
    """Return our landing page on itinal load"""
    return render(request, 'index.html')
    
    
def handler_404(request):
    data = {}
    return render(request, '404.html', data)


def handler_500(request):
    data = {}
    return render(request, '500.html', data)