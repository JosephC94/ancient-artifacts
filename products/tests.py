from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """All tests for the Product model are below"""
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')