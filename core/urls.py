from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home page
    path('', views.HomeView.as_view(), name='home'),
    
    # Products
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/category/<slug:category_slug>/', 
         views.ProductListView.as_view(), name='products_by_category'),
    path('product/<int:pk>/<slug:slug>/', 
         views.ProductDetailView.as_view(), name='product_detail'),
    
    # Contact
    path('contact/', views.ContactView.as_view(), name='contact'),
    
    # About
    path('about/', views.about_view, name='about'),
]
