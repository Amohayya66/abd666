from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', lambda request: render(request, 'home.html'), name='home'),

    # تضمين تطبيق الحسابات مع namespace
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]
