from django.test import TestCase
from product.serializers import ProductSerializer
from product.factories import CategoryFactory, ProductFactory

class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(name="technology")
        self.product = ProductFactory(
            name="Test Product",
            price=100.00,
            category=self.category
        )
        self.product_serializer = ProductSerializer(self.product)
    
    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["price"], "100.00")
        self.assertEqual(serializer_data["category_name"], "technology")
