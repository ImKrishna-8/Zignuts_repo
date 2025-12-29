from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    p_choice = [('high','high'),('medium','medium'),('low','low')]
    s_choice = [('complete','complete'),('rejected','rejected'),('pending','pending')]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    due_date = models.DateField(null=True,blank=True)
    priority = models.CharField(max_length=20,choices=p_choice)
    status = models.CharField(max_length=20,choices=s_choice)

    def __str__(self):
        return self.title