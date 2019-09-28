from django.test import TestCase
from .models import Feature


class FeatureEntryTest(TestCase):
    
    def test_string_representation(self):
        feature = Feature(title="TestFeature")
        self.assertEqual(str(feature), feature.title)
