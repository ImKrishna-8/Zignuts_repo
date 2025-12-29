from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields=['id','title','description','due_date','priority','status']

