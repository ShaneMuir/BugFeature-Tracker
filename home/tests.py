from django.test import TestCase
from .views import index

# Create your tests here.

class TestHomePage(TestCase):
    """
    Test that our home back returns the correct
    status
    """
    def test_home_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'index.html')