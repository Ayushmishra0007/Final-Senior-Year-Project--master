import os
import dj_database_url
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") != "False"
ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOST", "*")]

# APPLICATIONS
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.sites',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'parler',
    'paypal.standard.ipn',
    'crispy_forms',
    'sorl.thumbnail',
    'newsletter',
    'tinymce',
    'django_extensions',
    'watson',
    'import_export',

    'home',
    'about',
    'contact',
    'faq',
    'privacy-policy',
    'refund-policy',
    'onlineshop',
    'cart',
    'orders',
    'payment',
    'coupons',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eshopper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'eshopper.wsgi.application'

# DATABASE
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:admin@localhost:5432/eshopper'
    )
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# I18N
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Accra'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('zh-cn', _('Chinese')),
    ('pt', _('Portuguese')),
    ('ru', _('Russian')),
    ('nl', _('Dutch')),
    ('ko', _('Korean')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('fr', _('French')),
    ('de', _('German')),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# EMAIL
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "")
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = 'E-Shopper <noreply@eshopper.com>'

# CART
CART_SESSION_ID = 'cart'

# PAYPAL
PAYPAL_RECEIVER_EMAIL = os.environ.get("PAYPAL_RECEIVER_EMAIL", "")
PAYPAL_TEST = True

# REDIS
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

# PARLER
PARLER_LANGUAGES = {
    1: [{'code': lang[0]} for lang in LANGUAGES],
    'default': {'fallback': 'en', 'hide_untranslated': False},
}

# JET DASHBOARD
JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
JET_DEFAULT_THEME = 'light-gray'
JET_THEMES = [
    {'theme': 'default', 'color': '#47bac1', 'title': 'Default'},
    {'theme': 'green', 'color': '#44b78b', 'title': 'Green'},
    {'theme': 'light-green', 'color': '#2faa60', 'title': 'Light Green'},
    {'theme': 'light-violet', 'color': '#a464c4', 'title': 'Light Violet'},
    {'theme': 'light-blue', 'color': '#5EADDE', 'title': 'Light Blue'},
    {'theme': 'light-gray', 'color': '#222', 'title': 'Light Gray'},
]
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')

# REGISTRATION
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[E-Shopper]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False
SITE_ID = 1
LOGIN_REDIRECT_URL = '/profile'
LOGOUT_REDIRECT_URL = '/'
SIGNUP_REDIRECT_URL = '/profile'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# NEWSLETTER
NEWSLETTER_EMAIL_DELAY = 0.1
NEWSLETTER_BATCH_DELAY = 60
NEWSLETTER_BATCH_SIZE = 100
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"
