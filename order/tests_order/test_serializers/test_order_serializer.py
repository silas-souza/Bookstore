from django.test import TestCase
from django.contrib.auth.models import User
from order.models import Order
from order.serializers import OrderSerializer
from product.factories import ProductFactory, CategoryFactory

class TestOrderSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.category = CategoryFactory(name="books")
        self.product = ProductFactory(
            name="Test Book",
            price=29.99,
            category=self.category
        )
        self.order = Order.objects.create(user=self.user)
        self.order.product.add(self.product)
        self.order_serializer = OrderSerializer(self.order)
    
    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertIsNotNone(serializer_data)
