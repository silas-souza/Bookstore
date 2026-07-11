from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Category, Product
from order.models import Order
from order.serializers import OrderSerializer
from product.factories import CategoryFactory, ProductFactory

class OrderTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory(name='Books')
        self.product = ProductFactory(
            name='Test Book',
            price=29.99,
            category=self.category
        )
        self.order = Order.objects.create(
            product=self.product,
            quantity=2,
            total_price=59.98
        )

    def test_order_serializer_integrity(self):
        serializer = OrderSerializer(self.order)
        self.assertEqual(serializer.data['quantity'], 2)
        self.assertEqual(serializer.data['total_price'], '59.98')

    def test_order_creation(self):
        order = Order.objects.create(
            product=self.product,
            quantity=3,
            total_price=89.97
        )
        self.assertEqual(order.quantity, 3)

    def test_order_relationship_with_product(self):
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(str(self.order), f'Order {self.order.id} - {self.product.name}')
