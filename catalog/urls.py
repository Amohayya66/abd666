from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home_view, name='home'),  # ✅ هذا هو الحل الصحيح
    path('products/', views.product_list_view, name='product_list'),
]
