from django import template
from django.urls import resolve, reverse
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag(takes_context=True)
def active_link(context, view_name, *args, **kwargs):
    """
    Returns 'active' if the current URL matches the given view name.
    Usage: {% active_link 'view_name' %}
    """
    request = context.get('request')
    if not request:
        return ''
        
    # Get the current URL name
    current_url = resolve(request.path_info).url_name
    
    # Check if the current URL matches the given view name
    if current_url == view_name:
        return 'active'
    
    # For namespaced URLs
    if ':' in view_name:
        namespace, url_name = view_name.split(':')
        if current_url == url_name and resolve(request.path_info).namespace == namespace:
            return 'active'
    
    return ''
