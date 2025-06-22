import unittest
from unittest.mock import patch
from greyhoundDashboard.core.services.service_registry import ServiceDefinitions, ServiceDefinition

class TestServiceDefinitions(unittest.TestCase):

    def test_get_existing_definition(self):
        definition = ServiceDefinitions.get_definition('portainer')
        self.assertIsInstance(definition, ServiceDefinition)
        self.assertEqual(definition.name, 'Portainer')
        self.assertEqual(definition.enhanced_auth_fields, ['username', 'password'])
        self.assertIsNotNone(definition.service_class)

    def test_get_nonexistent_definition(self):
        definition = ServiceDefinitions.get_definition('nonexistent')
        self.assertIsNone(definition)

    def test_definitions_structure(self):
        keys = [key for key, _ in ServiceDefinitions._definitions]
        self.assertIn('portainer', keys)
        self.assertIn('navidrome', keys)
        self.assertIn('vikunja', keys)
        self.assertIn('proxmox', keys)
        self.assertIn('custom', keys)

    @patch('core.services.enhanced_services.EnhancedPortainer')
    def test_portainer_enhanced_class_mocked(self, mock_enhanced):
        definition = ServiceDefinitions.get_definition('portainer')
        self.assertIsNotNone(definition.service_class)
        self.assertEqual(definition.enhanced_auth_fields, ['username', 'password'])

if __name__ == '__main__':
    unittest.main()
