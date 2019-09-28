from django.test import TestCase
from .models import Order


class CheckoutEntryTest(TestCase):
    
    
    def test_string_representation(self):
        order = Order(full_name="abc", phone_number="123", street_address1="abc",
        postcode="abc")
        self.assertEqual(str(order.full_name), order.full_name)

