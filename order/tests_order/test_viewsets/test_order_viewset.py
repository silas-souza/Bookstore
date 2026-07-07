from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product, Category

class TestOrderViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.client.force_authenticate(user=self.user)
        
        # Criar category primeiro
        self.category = Category.objects.create(name="Books")
        
        self.product = Product.objects.create(
            name="Test Book",
            price=29.99,
            category=self.category  # Adicionar category
        )
        self.order_data = {
            "product": [self.product.id],
            "user": self.user.id
        }
    
    def test_order(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_create_order(self):
        url = reverse('order-list')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, 201)
