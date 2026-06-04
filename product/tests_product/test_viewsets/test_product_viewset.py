from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from product.factories import CategoryFactory, ProductFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        # Criar token corretamente
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.category = CategoryFactory(name="Electronics")
        self.product_data = {
            "name": "Laptop",
            "price": 999.99,
            "category": self.category.id
        }
    
    def test_get_all_product(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_create_product(self):
        url = reverse('product-list')
        response = self.client.post(url, self.product_data, format='json')
        self.assertEqual(response.status_code, 201)
