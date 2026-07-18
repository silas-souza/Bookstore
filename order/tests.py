from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from product.models import Category, Product
from product.factories import CategoryFactory, ProductFactory
from order.models import Order
from order.serializers import OrderSerializer


class OrderTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = CategoryFactory(name='Books')
        self.product = ProductFactory(
            name='Test Book',
            price=29.99,
            category=self.category
        )

    def test_order_serializer(self):
        order = Order.objects.create(
            product=self.product,
            quantity=2,
            total_price=59.98
        )
        serializer = OrderSerializer(order)
        self.assertEqual(serializer.data['quantity'], 2)

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            'product': self.product.id,
            'quantity': 3,
            'total_price': '89.97'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)

    def test_get_orders(self):
        Order.objects.create(
            product=self.product,
            quantity=1,
            total_price=29.99
        )
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
