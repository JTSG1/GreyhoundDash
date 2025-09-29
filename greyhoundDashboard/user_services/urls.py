from django.urls import path
from user_services import views


urlpatterns = [
    # Add your URL patterns here
    # Example:
    path('component/service-description/', views.component_service_description, name='service_description'),
    path('component/service/<str:registered_service>/', views.component_service_pill, name='service_pill'),
    path('component/service/enhanced/<str:registered_service>/', views.component_enhanced_service_data, name='service_call'),
]