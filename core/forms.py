from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from .models import ContactMessage, Product


class ContactForm(forms.ModelForm):
    """Contact form for the contact page"""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Your Name',
                'required': 'required',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'validate',
                'placeholder': 'Your Email',
                'required': 'required',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Subject',
                'required': 'required',
            }),
            'message': forms.Textarea(attrs={
                'class': 'materialize-textarea',
                'placeholder': 'Your Message',
                'required': 'required',
                'rows': 5,
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom classes and attributes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
            if field.required:
                field.widget.attrs['required'] = 'required'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")
        return email.lower()
    
    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise ValidationError("Name is required.")
        return name


class ProductInquiryForm(forms.Form):
    ""
    Form for product inquiries that pre-fills the subject with product information
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'placeholder': 'Your Name',
            'required': 'required',
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'validate',
            'placeholder': 'Your Email',
            'required': 'required',
        })
    )
    
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'placeholder': 'Phone Number (Optional)',
        }),
        validators=[
            RegexValidator(
                regex='^[\d\s\-+\(\)]+$',
                message='Please enter a valid phone number',
                code='invalid_phone'
            ),
        ]
    )
    
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'validate',
            'min': '1',
            'value': '1',
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'materialize-textarea',
            'placeholder': 'Your inquiry about this product...',
            'rows': 4,
        }),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        
        if self.product:
            self.fields['subject'] = forms.CharField(
                initial=f"Inquiry about {self.product.name}",
                widget=forms.HiddenInput()
            )
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity', 1)
        if self.product and quantity > self.product.stock:
            raise ValidationError(f"Only {self.product.stock} items available in stock.")
        return quantity


class NewsletterSignupForm(forms.Form):
    ""Form for newsletter signup"""
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'validate',
            'placeholder': 'Enter your email',
            'required': 'required',
        })
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower().strip()
        if not email:
            raise ValidationError("Email is required.")
        return email


class SearchForm(forms.Form):
    ""Search form for the products page"""
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'placeholder': 'Search products...',
            'aria-label': 'Search',
        })
    )
    
    category = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            'class': 'browser-default',
        })
    )
    
    sort = forms.ChoiceField(
        required=False,
        choices=[
            ('name', 'Name (A-Z)'),
            ('price_asc', 'Price (Low to High)'),
            ('price_desc', 'Price (High to Low)'),
            ('newest', 'Newest First'),
        ],
        widget=forms.Select(attrs={
            'class': 'browser-default',
            'onchange': 'this.form.submit()',
        })
    )
    
    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories', [])
        super().__init__(*args, **kwargs)
        
        # Set up category choices
        category_choices = [('', 'All Categories')]
        category_choices.extend([(cat.slug, cat.name) for cat in categories])
        self.fields['category'].choices = category_choices
        
        # Set initial values from GET parameters
        if 'data' not in kwargs:
            self.fields['q'].initial = self.initial.get('q', '')
            self.fields['category'].initial = self.initial.get('category', '')
            self.fields['sort'].initial = self.initial.get('sort', 'name')
