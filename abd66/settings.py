from pathlib import Path
import os
import cloudinary
from django.contrib.messages import constants as messages
import logging

# ====== المسار الأساسي ======
BASE_DIR = Path(__file__).resolve().parent.parent

# ====== إعدادات Cloudinary ======
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

# ====== إعدادات الأمان ======
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1']

# ====== ALLOWED_HOSTS ======
if DEBUG:
    ALLOWED_HOSTS = []
else:
    raw_hosts = os.getenv('ALLOWED_HOSTS', '')
    ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(',') if host.strip()]
    if not ALLOWED_HOSTS:
        ALLOWED_HOSTS = ['abd666.onrender.com']

# ====== التطبيقات ======
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'catalog',
    'orders',
    'accounts',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# ====== الوسيط ======
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ====== إعدادات العناوين ======
ROOT_URLCONF = 'abd66.urls'

# ====== إعدادات القوالب ======
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ====== WSGI ======
WSGI_APPLICATION = 'abd66.wsgi.application'

# ====== قاعدة البيانات ======
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'abd66_db_86j7',
            'USER': 'abd66_user',
            'PASSWORD': 'pMDXITqNhQeKW8tXtFsrwAbhkH0niOUm',
            'HOST': 'dpg-d1c1g3ur433s7380nmng-a.oregon-postgres.render.com',
            'PORT': '5432',
            'OPTIONS': {
                'sslmode': 'require'
            }
        }
    }

# ====== التحقق من كلمات المرور ======
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
]

# ====== اللغة والتوقيت ======
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ====== الملفات الثابتة ======
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ====== الوسائط ======
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ====== Cloudinary Storage ======
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ====== الرسائل ======
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# ====== تسجيل الأخطاء ======
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}
     