from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    address = models.TextField(blank=True, verbose_name="العنوان")
    phone = models.CharField(max_length=15, blank=True, verbose_name="رقم الجوال")

    def __str__(self):
        return self.user.username
