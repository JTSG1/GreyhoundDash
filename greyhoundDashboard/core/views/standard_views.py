from django.http import HttpResponse
from django.shortcuts import render
from core.models import RegisteredService

# Create your views here.
def index(request):

    services = RegisteredService.objects.all()

    return render(request, 'index.html', {'services': services})

def settings(request):
    """
    Render the settings page.
    """

    services = RegisteredService.objects.all()
        
    context = {
        'services': services,
    }

    return render(request, 'settings.html', context)

