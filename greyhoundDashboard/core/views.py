from django.http import HttpResponse
from django.shortcuts import render
from .models import RegisteredService
from .services.service_registry import ServiceDefinitions

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

def get_registered_service(func):
    """
    Decorator to retrieve the registered service from the database.
    """
    def wrapper(request, *args, **kwargs):
        service_id = kwargs.get('registered_service')
        try:
            registered_service = RegisteredService.objects.get(id=service_id)
        except RegisteredService.DoesNotExist:
            return render(request, '404.html', {'error': 'Service not found'}, status=404)
        
        return func(request, registered_service)
    
    return wrapper

@get_registered_service
def component_service_pill(request, registered_service: RegisteredService):

    include_assets = request.headers.get("x-include-assets", "true").lower() == "true"

    context = {
        'service': registered_service,
        'include_assets' : include_assets
    }

    return render(request, 'components/service-pill.html', context)

@get_registered_service
def component_enhanced_service_data(request, registered_service: RegisteredService):
    service_def = registered_service.definition

    if service_def is None:
        return render(request, '404.html', {'error': 'Service definition not registered'}, status=404)

    service_instance = registered_service.service_class.get()

    if not service_def.is_enhanced:
        return render(request, 'components/basic-service.html', service_instance.state, status=200)

    result = service_instance.render()
    if result is None:
        return HttpResponse("Service not available or not implemented.", status=503)

    return render(request, 'components/enhanced-service-data.html', {
        'service': service_def,
        'result': result,
    })