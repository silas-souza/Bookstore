from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer
from product.models import Product

class TestProductViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.category = CategoryFactory()

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': 'Smart TV',
            'description': '4K OLED TV',
            'price': '2000.00',
            'stock': 10,
            'category': self.category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)

    def test_get_all_product(self):
        ProductFactory.create_batch(3, category=self.category)
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
