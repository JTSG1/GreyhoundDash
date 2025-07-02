import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "greyhoundDashboard.settings")
django.setup()

from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import RegisteredService
from core.services.service_registry import ServiceDefinitions

class RegisteredServiceModelTests(TestCase):

    def test_str_method_returns_name(self):
        service = RegisteredService(name="Test Service", service_type="portainer")
        self.assertEqual(str(service), "Test Service")

    def test_save_sets_default_auth_fields_for_enhanced_service(self):
        service = RegisteredService(name="Navidrome", service_type="navidrome")
        service.save()
        expected_fields = ServiceDefinitions.get_definition('navidrome').enhanced_auth_fields
        self.assertTrue(all(field in service.auth_fields for field in expected_fields))
        self.assertTrue(all(service.auth_fields[field] == '' for field in expected_fields))

    def test_save_raises_value_error_for_invalid_service_type(self):
        service = RegisteredService(name="Invalid", service_type="fake-service")
        with self.assertRaises(ValueError) as context:
            service.save()
        self.assertIn("Invalid service type", str(context.exception))

    def test_save_raises_error_if_auth_fields_is_not_dict(self):
        service = RegisteredService(name="Vikunja", service_type="vikunja", auth_fields="not_a_dict")
        with self.assertRaises(ValueError) as context:
            service.save()
        self.assertIn("auth_fields must be a dictionary", str(context.exception))

    def test_save_preserves_existing_auth_fields(self):
        service = RegisteredService(
            name="Portainer",
            service_type="portainer",
            auth_fields={"username": "admin", "password": "secret"}
        )
        service.save()
        self.assertEqual(service.auth_fields["username"], "admin")
        self.assertEqual(service.auth_fields["password"], "secret")
