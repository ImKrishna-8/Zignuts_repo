from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='pizzas/')
    info = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('order_received', 'Order Received'),
        ('preparing', 'Preparing'),
        ('baking', 'Baking'),
        ('out_for_delivery', 'Out For Delivery'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='order_received'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    def save(self,*args, **kwargs):
        is_new = self.pk is None

        super().save(*args, **kwargs)

        if not is_new:
            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                f'order_{self.id}',{
                    'type':'update_status',
                    'status':self.status
                }
            )




class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Price at the time of order"
    )

    def __str__(self):
        return f"{self.quantity} x {self.pizza.name}"
