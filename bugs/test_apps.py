from django.apps import apps
from django.test import TestCase
from bugs.apps import BugsConfig


class BugsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(BugsConfig.name, 'bugs')
        self.assertEqual(apps.get_app_config('bugs').name, 'bugs')