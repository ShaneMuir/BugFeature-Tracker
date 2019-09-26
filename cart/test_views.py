from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client
from features.models import Feature

class TestViews(TestCase):
    """Set of tests to be performed agaist our views"""
    
    def setUp(self):
        """Logs in a user for our tests"""
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")


    def test_status_codes(self):
        """Test that our app returns status_codes 200 and 404"""
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
        
        page = self.client.get('/carty/')
        self.assertEqual(page.status_code, 404)
        self.assertTemplateNotUsed(page, 'cart.html')

    
    def test_add_to_cart(self):
        """Test that we can add items to our cart"""
        user = User(username="admin")
        user.save()

        feature = Feature(title="test", description="testing", creator=user)
        feature.save()
        
        page = self.client.get('/cart/add/{0}'.format(feature.id))
        self.assertEqual(page.status_code, 301)