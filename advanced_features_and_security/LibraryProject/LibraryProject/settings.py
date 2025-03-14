"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=0ybu&ul#d0&kqr7&yli%wxmobdx2re1f51t@1%a8@6v21mtb9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# Security Headers
SECURE_BROWSER_XSS_FILTER = True  # Protects against XSS attacks
X_FRAME_OPTIONS = 'DENY'  # Prevents Clickjacking attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing

# Enforce HTTPS-only cookies
CSRF_COOKIE_SECURE = True  # CSRF cookie will only be sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookie will only be sent over HTTPS

# Content Security Policy (CSP) using django-csp middleware
INSTALLED_APPS += ['csp']

CSP_DEFAULT_SRC = ("'self'",)  # Only allow resources from the same domain
CSP_SCRIPT_SRC = ("'self'", "https://trusted-cdn.com")  # Allow scripts from self and a trusted CDN
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://trusted-styles.com")
CSP_IMG_SRC = ("'self'", "data:")
CSP_FRAME_ANCESTORS = ("'none'",)  # Prevents embedding in iframes

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',  # Enable CSP protection
]

# Ensure HTTPS usage (for production)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_HTTPONLY = True  # Prevents JavaScript access to session cookie
CSRF_COOKIE_HTTPONLY = True  # Prevents JavaScript access to CSRF cookie
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure Django recognizes HTTPS when behind a proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Redirect all HTTP traffic to HTTPS (ensure this is True in production)
SECURE_SSL_REDIRECT = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
