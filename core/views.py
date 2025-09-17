from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import Product, Category, ContactMessage


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get featured products, ordered by most recently added
        context['featured_products'] = Product.objects.filter(
            featured=True, 
            available=True
        ).order_by('-created_at')[:3]
        
        # Get categories for the dropdown
        context['categories'] = Category.objects.all()[:6]
        return context


class ProductListView(ListView):
    """Product list view with search and filter functionality"""
    model = Product
    template_name = 'core/products.html'
    context_object_name = 'products'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        
        # Search functionality
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )
        
        # Category filter
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        
        # Sort by price, name, etc.
        sort_by = self.request.GET.get('sort', 'name')
        if sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort_by == 'newest':
            queryset = queryset.order_by('-created_at')
        else:
            queryset = queryset.order_by('name')
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.kwargs.get('category_slug', '')
        context['search_query'] = self.request.GET.get('q', '')
        context['sort_by'] = self.request.GET.get('sort', 'name')
        return context


class ProductDetailView(DetailView):
    """Product detail view"""
    model = Product
    template_name = 'core/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related products (same category, excluding current product)
        product = self.get_object()
        context['related_products'] = Product.objects.filter(
            category=product.category,
            available=True
        ).exclude(id=product.id)[:4]
        return context


class ContactView(CreateView):
    """Contact form view"""
    model = ContactMessage
    template_name = 'core/contact.html'
    fields = ['name', 'email', 'subject', 'message']
    success_url = reverse_lazy('core:contact')
    
    def form_valid(self, form):
        # Send email notification first
        subject = f"New Contact Form Submission: {form.cleaned_data['subject']}"
        message = f"""
        Name: {form.cleaned_data['name']}
        Email: {form.cleaned_data['email']}
        
        Message:
        {form.cleaned_data['message']}
        """
        print('EMAIL_BACKEND:', settings.EMAIL_BACKEND)
        print('DEFAULT_FROM_EMAIL:', settings.DEFAULT_FROM_EMAIL)
        print('CONTACT_EMAIL:', settings.CONTACT_EMAIL)
        print('EMAIL_HOST:', getattr(settings, 'EMAIL_HOST', None))
        print('EMAIL_PORT:', getattr(settings, 'EMAIL_PORT', None))
        print('EMAIL_HOST_USER:', getattr(settings, 'EMAIL_HOST_USER', None))
        print('EMAIL_USE_TLS:', getattr(settings, 'EMAIL_USE_TLS', None))
        print('EMAIL_HOST_PASSWORD:', getattr(settings, 'EMAIL_HOST_PASSWORD', None))
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        # Only save if email sent successfully
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Thank you for your message! We will get back to you soon.'
        )
        return response


def about_view(request):
    """About page view"""
    return render(request, 'core/about.html')
