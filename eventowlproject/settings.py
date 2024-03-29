import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.getenv("SECRET_KEY", "verysecret")
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'email_html',
    'account',
    'widget_tweaks',
    'django_js_reverse',
    'eventowl',
    'concertowl',
    'bookowl',
    'notifications',
    'django_celery_results',
]

APPS_WITH_PREVIEW = (
    'concertowl',
    'bookowl',
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'eventowlproject.middleware.LoginRequiredMiddleware'
]

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
    SECURE_SSL_REDIRECT = True
    MIDDLEWARE.insert(
        0, 'django.middleware.security.SecurityMiddleware'
    )

ROOT_URLCONF = 'eventowlproject.urls'

WSGI_APPLICATION = 'eventowlproject.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///./db.sqlite')
}

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'Europe/Berlin'
USE_TZ = False

IS_LOCAL = os.getenv('IS_LOCAL', "True") == "True"

TEMPLATE_SETTINGS = ['IS_LOCAL', 'MAX_UPLOAD_SIZE_MB']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account'
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "provided_static"),
)
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

PAGINATION_SIZE = 100

MAX_UPLOAD_SIZE_MB = 2
MAX_UPLOAD_SIZE = MAX_UPLOAD_SIZE_MB * 1024 ** 2

EMAIL_SUBJECT_PREFIX = "[EventOwl] "
DEFAULT_FROM_EMAIL = "eventowl@{}".format(
    os.getenv('SPARKPOST_SANDBOX_DOMAIN', 'eventowl.com')
)

EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('SPARKPOST_SMTP_HOST')
EMAIL_PORT = int(os.getenv('SPARKPOST_SMTP_PORT', 465))
EMAIL_HOST_USER = os.getenv('SPARKPOST_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SPARKPOST_SMTP_PASSWORD')

DAYS_BACK = 3

LOGIN_URL = '/account/signup'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_EXEMPT_URLS = (
    r'admin/+',
    r'account/(login|signup|password/reset)/+',
    r'account/add_profile/.*',
    r'account/confirm_email/.*',
    r'login.*',
    r'complete.*',
    r'about/+$',
    r'impressum/+$',
    r'feed/.*',
    r'calendar/.*'
)

SITE_ID = 1

NUMBER_OF_PREVIEW_OBJECTS = 6

DJANGO_NOTIFICATIONS_CONFIG = {'USE_JSONFIELD': True}

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO' if DEBUG else 'INFO',
            'propagate': True,
        },
    }
}
