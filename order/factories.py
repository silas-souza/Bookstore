import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from order.models import Order
from product.factories import ProductFactory

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
    
    user = factory.SubFactory(UserFactory)
    
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.product.add(product)
