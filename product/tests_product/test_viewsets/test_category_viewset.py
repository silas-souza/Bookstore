from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from product.factories import CategoryFactory
from product.models import Category

class CategoryViewSet(APITestCase):
    def setUp(self):
        # Criar usuário e autenticar
        self.user = User.objects.create_user(
            username="admin",
            password="admin123",
            is_staff=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.category = CategoryFactory(name="books")
    
    def test_get_all_category(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_create_category(self):
        url = reverse('category-list')
        data = {
            "name": "Technology"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
