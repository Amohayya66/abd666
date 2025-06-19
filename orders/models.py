from django.db import models
from django.conf import settings
from catalog.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="العميل")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    is_paid = models.BooleanField(default=False, verbose_name="تم الدفع")

    def __str__(self):
        return f"طلب رقم {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر عند الطلب")

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
