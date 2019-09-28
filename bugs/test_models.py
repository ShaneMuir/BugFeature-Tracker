from django.test import TestCase
from .models import Bug


class BugEntryTest(TestCase):
    
    def test_string_representation(self):
        bug = Bug(title="TestBug")
        self.assertEqual(str(bug), bug.title)
