from django.core.management.base import BaseCommand
from core.models import Category, Product

class Command(BaseCommand):
    help = 'Load sample data for D&S Karans Ltd website'

    def handle(self, *args, **options):
        # Create categories
        kava_category = Category.objects.create(
            name='Kava',
            slug='kava',
            description='Premium kava products from the Pacific Islands'
        )
        
        spices_category = Category.objects.create(
            name='Spices',
            slug='spices',
            description='Exotic spices from around the world'
        )
        
        tea_category = Category.objects.create(
            name='Tea',
            slug='tea',
            description='Fine teas from various regions'
        )
        
        # Create sample products
        Product.objects.create(
            name='Premium Fijian Kava',
            slug='premium-fijian-kava',
            category=kava_category,
            description='The finest Fijian kava, traditionally prepared and sun-dried.',
            price=49.99,
            stock=100,
            available=True,
            featured=True
        )
        
        Product.objects.create(
            name='Vanuatu Kava',
            slug='vanuatu-kava',
            category=kava_category,
            description='Strong and smooth kava from the islands of Vanuatu.',
            price=54.99,
            stock=75,
            available=True,
            featured=True
        )
        
        Product.objects.create(
            name='Premium Turmeric Powder',
            slug='premium-turmeric-powder',
            category=spices_category,
            description='High-quality turmeric powder with rich color and flavor.',
            price=12.99,
            stock=200,
            available=True,
            featured=True
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data!'))
