from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_services.models import RegisteredService
from user_services.registry.service_registry import ServiceDefinitions
from dashboard.forms.registered_service import NewRegisteredServiceForm
from common.utils import get_registered_service

def new_registered_service_form(request):
    
    if request.method == 'POST':

        id = request.POST.get('id', None)
        registered_service = None
        if id:
            try:
                registered_service = RegisteredService.objects.get(id=id)
            except RegisteredService.DoesNotExist:
                return render(request, '404.html', {'error': 'Service not found'}, status=404)

        form = NewRegisteredServiceForm(request.POST, instance=registered_service)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            header = {
                "HX-Refresh": "true",
            }
            return HttpResponse("<div>Form submitted successfully!</div>", status=200, headers=header)
    else:
        form = NewRegisteredServiceForm()

    return render(request, 'components/settings/new-registered-service-form.html', {'form': form})

def edit_registered_service_form(request, registered_service_id):
    """
    Render the form to edit an existing registered service.
    """
    try:
        registered_service = RegisteredService.objects.get(id=registered_service_id)
    except RegisteredService.DoesNotExist:
        return render(request, '404.html', {'error': 'Service not found'}, status=404)

    if request.method == 'POST':
        form = NewRegisteredServiceForm(request.POST, instance=registered_service)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            header = {
                "HX-Refresh": "true",
            }
            return HttpResponse("<div>Form submitted successfully!</div>", status=200, headers=header)
    else:
        form = NewRegisteredServiceForm(instance=registered_service)

    return render(request, 'components/settings/new-registered-service-form.html', {'form': form})

@get_registered_service
def component_confirm_delete_dialogue(request, registered_service: RegisteredService):


    return render(request, "components/settings/confirm-delete-dialogue.html", { "service" : registered_service }, status=200)


@get_registered_service
def component_perform_delete(request, registered_service: RegisteredService):

    registered_service.delete()

    return redirect("settings")