from django.urls import path
from core import views


urlpatterns = [
    # Add your URL patterns here
    # Example:
    path('', views.index, name='index'),
    path('component/service/<str:registered_service>/', views.component_service_pill, name='service_pill'),
    path('component/service/enhanced/<str:registered_service>/', views.component_enhanced_service_data, name='service_call'),
]