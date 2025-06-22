from django.http import HttpResponse
from django.shortcuts import render
from .models import RegisteredService
from .services.service_registry import ServiceDefinitions

# Create your views here.
def index(request):

    services = RegisteredService.objects.all()

    return render(request, 'index.html', {'services': services})

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

    service = ServiceDefinitions.get_definition(registered_service.service_type)
    if service is not None and not service.is_enhanced:
        basic_service = service.service_class(registered_service).get()
        return render(request, 'components/basic-service.html', basic_service.state, status=200)
    if service is None:
        return render(request, '404.html', {'error': 'Service definition not registered'}, status=200)
    # If the service has an enhanced version, instantiate it
    result = None
    if service.is_enhanced:
        result = service.service_class(registered_service).get().render()

    if result is None:
        return HttpResponse("Service not available or not implemented.", status=503)
    else:
        return render(request, 'components/enhanced-service-data.html', {'service': service, 'result': result})