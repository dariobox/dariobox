from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from access.models import User

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product_name = models.CharField(max_length=255, null=False)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], null=False)
    order_date = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.product_name}"
