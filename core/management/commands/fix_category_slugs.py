from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import Category

class Command(BaseCommand):
    help = 'Fix empty or invalid category slugs'

    def handle(self, *args, **options):
        # Get all categories with empty or None slugs
        categories = Category.objects.filter(slug__isnull=True) | Category.objects.filter(slug__exact='')
        
        updated_count = 0
        
        for category in categories:
            old_slug = category.slug
            category.slug = slugify(category.name)
            
            # Ensure the slug is unique
            original_slug = category.slug
            counter = 1
            while Category.objects.filter(slug=category.slug).exclude(id=category.id).exists():
                category.slug = f"{original_slug}-{counter}"
                counter += 1
            
            category.save()
            updated_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Updated category "{category.name}" slug from "{old_slug}" to "{category.slug}"')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {updated_count} category slugs')
        )
