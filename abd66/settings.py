from pathlib import Path
import cloudinary  # ← استيراد مكتبة cloudinary
import os

# إعداد Cloudinary الأساسي (مطلوب من المكتبة الأصلية)
cloudinary.config( 
  cloud_name = 'dcoutuiif', 
  api_key = '713926589539725', 
  api_secret = 'IYgGlpoD5CmUv5fR4GTYTnpJZHs' 
)

# المسار الرئيسي
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان (لا تنشره في الإنتاج!)
SECRET_KEY = 'django-insecure-REPLACE_THIS_WITH_A_SECURE_KEY'

DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقاتك
    'catalog',
    'orders',
    'accounts',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',
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

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# إعدادات Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dcoutuiif',
    'API_KEY': '713926589539725',
    'API_SECRET': 'IYgGlpoD5CmUv5fR4GTYTnpJZHs',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# إعدادات الوسائط
MEDIA_URL = '/media/'

# إعدادات الرسائل
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
