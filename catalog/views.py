from django.shortcuts import render
from .models import Product

def home_view(request):
    """
    يعرض الصفحة الرئيسية ويمرر المنتجات لعرضها أسفل البنر.
    """
    products = Product.objects.select_related('category').all().order_by('-created_at')
    return render(request, 'home.html', {
        'products': products
    })

def product_list_view(request):
    """
    يعرض صفحة قائمة المنتجات المستقلة.
    """
    products = Product.objects.select_related('category').all().order_by('-created_at')
    return render(request, 'catalog/product_list.html', {
        'products': products
    })
