from django.apps import apps
from django.test import TestCase
from features.apps import FeaturesConfig


class FeaturesConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(FeaturesConfig.name, 'features')
        self.assertEqual(apps.get_app_config('features').name, 'features')