from django.test import TestCase
from .forms import BugCommentForm, BugCreationForm

class TestBugCommentForm(TestCase):
    """Set of tests for our bug comment form"""
    
    def test_users_can_comment(self):
        form = BugCommentForm({'comment': 'Test comment'})
        self.assertTrue(form.is_valid())
        
    
    def test_form_cant_be_blank(self):
        form = BugCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], ['This field is required.'])

        

class TestBugCreationForm(TestCase):
    """A set of tests agaist our bug creation form"""
    def test_required_fields(self):
        form = BugCreationForm({'title':'', 'description': 'Bug description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])
        
        form = BugCreationForm({'title': 'Test title', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        
        
    def test_users_can_create_a_bug(self):
        form = BugCreationForm({'title': 'Bug Title',
                                'description': 'Bug description'})
        self.assertTrue(form.is_valid())
