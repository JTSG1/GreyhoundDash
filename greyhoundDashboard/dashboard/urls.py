from django.urls import path
from dashboard import views


urlpatterns = [
    # Add your URL patterns here
    # Example:
    path('', views.index, name='index'),
    path('services/', views.settings, name='settings'),
    path('services/service-admin/delete/<int:registered_service>', views.component_perform_delete, name='perform_delete'),
    path('component/settings/confirm-delete-dialogue/<int:registered_service>', views.component_confirm_delete_dialogue, name='confirm_delete_service'),
    path('component/new-registered-service-form/', views.new_registered_service_form, name='new_registered_service_form'),
    path('component/edit-registered-service-form/<int:registered_service_id>/', views.edit_registered_service_form, name='edit_registered_service_form'),
]