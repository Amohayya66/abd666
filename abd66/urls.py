from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('', include('catalog.urls')),  # يتطلب أن يحتوي catalog/urls.py على مسار فارغ ''
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
]

# دعم ملفات الصور عند استخدام ImageField
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
