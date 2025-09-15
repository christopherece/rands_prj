# D&S Karans Ltd - E-commerce Website

A modern e-commerce website for D&S Karans Ltd, an importer and distributor of premium Kava and other products.

## Features

- **Product Catalog**: Browse products by category with search and filtering
- **Product Details**: Detailed product pages with related items
- **Contact Form**: Easy way for customers to get in touch
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Admin Interface**: Manage products, categories, and messages
- **SEO Optimized**: Clean URLs, meta tags, and sitemap

## Tech Stack

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript, Materialize CSS
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Docker, Nginx, Gunicorn

## Prerequisites

- Python 3.9+
- PostgreSQL (for production)
- Node.js and npm (for frontend assets)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dskaranltd.git
   cd dskaranltd
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the admin panel**
   Visit http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

## Project Structure

```
dskaranltd/
├── core/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App config
│   ├── forms.py          # Forms
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   └── views.py          # View functions
├── dskaranltd/           # Project configuration
│   ├── settings/         # Settings for different environments
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py
├── media/                # User-uploaded files
├── static/               # Collected static files
├── templates/            # Global templates
├── .env                  # Environment variables
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Deployment

### Production

1. Set up a production environment:
   ```bash
   export DJANGO_ENV=production
   export DJANGO_SECRET_KEY=your-secret-key
   export DJANGO_DEBUG=False
   export DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   export DB_NAME=dbname
   export DB_USER=dbuser
   export DB_PASSWORD=dbpassword
   export DB_HOST=localhost
   export DB_PORT=5432
   ```

2. Install production dependencies:
   ```bash
   pip install -r requirements/production.txt
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. Set up your web server (Nginx + Gunicorn recommended)

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Secret key for Django | Required |
| `DJANGO_DEBUG` | Debug mode | `False` in production |
| `DJANGO_ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `DB_NAME` | Database name | - |
| `DB_USER` | Database user | - |
| `DB_PASSWORD` | Database password | - |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `EMAIL_HOST` | SMTP server | - |
| `EMAIL_HOST_USER` | SMTP username | - |
| `EMAIL_HOST_PASSWORD` | SMTP password | - |
| `EMAIL_PORT` | SMTP port | `587` |
| `EMAIL_USE_TLS` | Use TLS for SMTP | `True` |
| `DEFAULT_FROM_EMAIL` | Default sender email | `noreply@dskarans.com` |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Materialize CSS](https://materializecss.com/)
- [Unsplash](https://unsplash.com/) for sample images
