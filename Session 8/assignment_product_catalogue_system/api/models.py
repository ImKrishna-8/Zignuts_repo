from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY = [
        ('Electronics','Electronics'),('Tech','Tech'),('Home and appliance','Home and appliance'),('hardware','hardware'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    price = models.IntegerField(default=0)
    stock_quantity=models.IntegerField(default=1)
    category=models.CharField(choices=CATEGORY)

    def __str__(self):
        return self.name