
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields=['id','name','description','price','category','stock_quantity']

    def validate_price(self,value):
        if value<0:
            raise serializers.ValidationError('Price Should not be negative')
        return value