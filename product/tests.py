from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer
from product.factories import CategoryFactory, ProductFactory


class ProductAndCategoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Technology',
            description='Electronic devices'
        )
        self.product = Product.objects.create(
            name='Smartphone',
            description='Latest model',
            price=999.99,
            category=self.category,
            stock=50
        )

    def test_category_serializer_integrity(self):
        serializer = CategorySerializer(self.category)
        self.assertEqual(serializer.data['name'], 'Technology')

    def test_product_serializer_integrity(self):
        serializer = ProductSerializer(self.product)
        self.assertEqual(serializer.data['name'], 'Smartphone')
        self.assertEqual(serializer.data['category_name'], 'Technology')


class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='admin',
            password='admin123',
            is_staff=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.category = CategoryFactory()

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': 'New Product',
            'description': 'Test description',
            'price': '100.00',
            'stock': 10,
            'category': self.category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)

    def test_get_all_products(self):
        ProductFactory.create_batch(3, category=self.category)
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
