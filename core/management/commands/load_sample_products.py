from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils.text import slugify
import os
from core.models import Category, Product

class Command(BaseCommand):
    help = 'Load sample products into the database'

    def handle(self, *args, **options):
        # Create or get categories with valid slugs
        category1, created = Category.objects.get_or_create(
            slug=slugify('Beverages'),
            defaults={
                'name': 'Beverages',
                'description': 'Refreshing drinks from around the world',
            }
        )
        
        # Update slug if it was created without one
        if not created and not category1.slug:
            category1.slug = slugify(category1.name)
            category1.save()
        
        category2, created = Category.objects.get_or_create(
            slug=slugify('Snacks'),
            defaults={
                'name': 'Snacks',
                'description': 'Delicious snacks and treats',
            }
        )
        
        # Update slug if it was created without one
        if not created and not category2.slug:
            category2.slug = slugify(category2.name)
            category2.save()
        
        # Sample products data
        sample_products = [
            {
                'name': 'Premium Fijian Kava',
                'category': category1,
                'description': 'Experience the authentic taste of Fiji with our premium kava. Sourced from the finest Fijian kava plants, known for their smooth taste and relaxing effects.',
                'price': 29.99,
                'stock': 50,
                'available': True,
                'featured': True,
            },
            {
                'name': 'Tropical Dried Mango',
                'category': category2,
                'description': 'Sweet and chewy dried mango slices, naturally sun-dried to preserve their tropical flavor.',
                'price': 12.99,
                'stock': 100,
                'available': True,
                'featured': True,
            },
            {
                'name': 'Organic Coconut Chips',
                'category': category2,
                'description': 'Crunchy, lightly salted coconut chips made from organic coconuts. Perfect for snacking or topping desserts.',
                'price': 9.99,
                'stock': 75,
                'available': True,
                'featured': False,
            },
        ]
        
        # Add sample products
        for product_data in sample_products:
            slug = slugify(product_data['name'])
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'slug': slug,
                    'category': product_data['category'],
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'available': product_data['available'],
                    'featured': product_data['featured'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample products'))
