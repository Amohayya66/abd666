# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'  # ← هذه السطر هو المفتاح لحل المشكلة

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
