from django.test import TestCase
from django.contrib.auth.models import User
from product.factories import CategoryFactory, ProductFactory
from order.models import Order
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(name="books")
        self.product = ProductFactory(
            name="Test Book",
            price=29.99,
            category=self.category
        )
        self.order = Order.objects.create(
            product=self.product,
            quantity=2,
            total_price=59.98
        )

    def test_order_serializer(self):
        serializer = OrderSerializer(self.order)
        serializer_data = serializer.data
        self.assertEqual(serializer_data['product'], self.product.id)
        self.assertEqual(serializer_data['quantity'], 2)
        self.assertEqual(serializer_data['total_price'], '59.98')
