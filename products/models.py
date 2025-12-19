from django.db import models
from categories.models import Category
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
