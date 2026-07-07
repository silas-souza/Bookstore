import factory
from factory.django import DjangoModelFactory
from product.models import Category, Product

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
    
    name = factory.Faker('word')
    description = factory.Faker('text')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Faker('word')
    description = factory.Faker('text')
    price = factory.Faker('random_number', digits=2)
    category = factory.SubFactory(CategoryFactory)
