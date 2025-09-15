"""
Context processors for the core app.
"""
from django.conf import settings


def site_info(request):
    """
    Add site-wide information to the template context.
    """
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'D&S Karans Ltd'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'Premium Importer & Distributor'),
        'SITE_AUTHOR': getattr(settings, 'SITE_AUTHOR', 'D&S Karans Ltd'),
        'SITE_YEAR': getattr(settings, 'SITE_YEAR', '2024'),
        'CONTACT_EMAIL': getattr(settings, 'CONTACT_EMAIL', 'info@dskarans.com'),
    }
