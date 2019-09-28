from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User


class TestCheckoutViews(TestCase):
    """Set of test agaist our views"""
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        
    def test_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')