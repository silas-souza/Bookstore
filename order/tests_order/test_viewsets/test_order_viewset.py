from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from product.factories import CategoryFactory, ProductFactory
from order.models import Order

class TestOrderViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='admin',
            password='admin123',
            is_staff=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Criar categoria e produto para os testes
        self.category = CategoryFactory(name='Books')
        self.product = ProductFactory(
            name='Test Book',
            price=29.99,
            category=self.category
        )

        self.order_data = {
            'product': self.product.id,
            'quantity': 2,
            'total_price': '59.98'
        }

    def test_order(self):
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        url = reverse('order-list')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().quantity, 2)
        self.assertEqual(str(Order.objects.get().total_price), '59.98')
