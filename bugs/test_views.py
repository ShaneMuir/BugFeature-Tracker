from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client
from .models import Bug
from django.shortcuts import get_object_or_404


class TestBugViews(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        
    def test_all_bugs_page(self):
        response = self.client.get('/bugs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs.html')
        
        
    def test_single_bug_view(self):
        user = User.objects.get(username="test")
        bug = Bug(title="Test title", description="Test description",
                  creator_id=user.id)
        bug.save()
        response = self.client.get('/bugs/{}'.format(bug.id))
        self.assertEqual(response.status_code, 301)
        
    def test_create_bug_view(self):
        response = self.client.get('/bugs/create_bug/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_bug.html')
