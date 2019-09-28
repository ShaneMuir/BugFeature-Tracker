from django.apps import apps
from django.test import TestCase
from checkout.apps import CheckoutConfig


class TestCheckoutConfig(TestCase):
    """Test our apps"""
    def test_apps(self):
        self.assertEqual(CheckoutConfig.name, 'checkout')
        self.assertEqual(apps.get_app_config('checkout').name, 'checkout')