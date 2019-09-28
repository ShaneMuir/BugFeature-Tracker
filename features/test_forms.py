from django.test import TestCase
from .forms import FeatureCommentForm, FeatureCreationForm


class TestFeatureCommentForm(TestCase):
    """Set of tests for our feature comment form"""
    
    def test_users_can_comment(self):
        form = FeatureCommentForm({'comment': 'Test comment'})
        self.assertTrue(form.is_valid())
        
    
    def test_form_cant_be_blank(self):
        form = FeatureCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], ['This field is required.'])
        
        
class TestFeatureCreationForm(TestCase):
    """A set of tests agaist our feature creation form"""
    def test_required_fields(self):
        form = FeatureCreationForm({'title':'', 'description': 'Feature description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])
        
        form = FeatureCreationForm({'title': 'Test title', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        
        
    def test_users_can_create_a_bug(self):
        form = FeatureCreationForm({'title': 'Feature Title',
                                'description': 'Feature description'})
        self.assertTrue(form.is_valid())
