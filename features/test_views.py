from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Feature
from django.shortcuts import get_object_or_404


class TestFeatureViews(TestCase):
    """
    Set of test to ensure everything in our views is working
    correctly
    """
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        
    def test_all_features_page(self):
        response = self.client.get('/features/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features.html')
        
        
    def test_single_feature_view(self):
        user = User.objects.get(username="test")
        feature = Feature(title="Test title", description="Test description",
                  creator_id=user.id)
        feature.save()
        response = self.client.get('/features/{}'.format(feature.id))
        self.assertEqual(response.status_code, 301)
        
    def test_create_feature_view(self):
        response = self.client.get('/features/create_feature/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_feature.html')