from django.db import models
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    address = models.TextField()