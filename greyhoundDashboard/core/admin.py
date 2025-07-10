from django.contrib import admin

# Register your models here.
admin.site.site_header = "Greyhound Dashboard Admin"
admin.site.site_title = "Greyhound Dashboard Admin Portal"
admin.site.index_title = "Welcome to the Greyhound Dashboard Admin Portal"

from .models import RegisteredService, RegisteredServiceLog
 
# make some fields read-only
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'created_at', 'updated_at')
    search_fields = ('name', 'service_type')
    # readonly_fields = ('auth_fields', 'created_at', 'updated_at')

admin.site.register(RegisteredService, ServiceAdmin)

admin.site.register(RegisteredServiceLog)

