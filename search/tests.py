from django.test import TestCase, Client
from .views import search
from bugs.models import Bug
from django.contrib import auth
from django.contrib.auth.models import User

# Create your tests here.

class TestSearchPage(TestCase):
    """
    Test that our search page returns the correct
    status
    """
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        
    def test_search_page_is_rendered(self):
        user = User.objects.get(username="test")
        bug = Bug(title="test", description="testing", creator_id=user.id)
        bug.save()
        url = self.client.get('/search/?q=test')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'search.html')