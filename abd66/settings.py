from pathlib import Path
import os
import cloudinary
import dj_database_url

# ====== المسار الأساسي للمشروع ======
BASE_DIR = Path(__file__).resolve().parent.parent

# ====== إعدادات Cloudinary من .env ======
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', 'dcoutuiif'),
    api_key=os.getenv('CLOUDINARY_API_KEY', '713926589539725'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET', 'IYgGlpoD5CmUv5fR4GTYTnpJZHs')
)

# ====== أمان وبيئة ======
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-REPLACE_THIS_WITH_A_SECURE_KEY')
DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1', 'yes']

ALLOWED_HOSTS = []
if not DEBUG:
    hosts = os.getenv('ALLOWED_HOSTS', '')
    ALLOWED_HOSTS = [host.strip() for host in hosts.split(',') if host.strip()]

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

# ====== عناوين المشروع ======
ROOT_URLCONF = 'abd66.urls'

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
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True
        )
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

# ====== إعداد Cloudinary ======
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'dcoutuiif'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', '713926589539725'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', 'IYgGlpoD5CmUv5fR4GTYTnpJZHs'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ====== الوسائط ======
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ====== الرسائل ======
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
