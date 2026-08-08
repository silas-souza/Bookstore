from django.test import TestCase
from product.serializers import CategorySerializer
from product.factories import CategoryFactory

class TestCategorySerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(name="food")
        self.category_serializer = CategorySerializer(self.category)
    
    def test_order_serializer(self):
        serializer_data = self.category_serializer.data
        self.assertEqual(serializer_data["name"], "food")
