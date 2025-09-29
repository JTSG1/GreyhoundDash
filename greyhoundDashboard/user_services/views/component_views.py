from django.http import HttpResponse
from django.shortcuts import render
from common.utils import get_registered_service
from user_services.models import RegisteredService
from user_services.registry.service_registry import ServiceDefinitions

def component_service_description(request):
    """
    Render the service description based on the selected service type.
    """
    service_type = request.GET.get('service_type', None)
    
    if service_type:
        description = ServiceDefinitions.get_description(service_type)
        return render(request, 'components/service-description.html', {
            'service_type': service_type,
            'description': description,
        })
    
    return HttpResponse("No service type provided.", status=400)

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
