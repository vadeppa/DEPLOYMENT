from django.db import models

# Create your models here.
class Employee(models.Model):
    Query=models.CharField(max_length=20)
    Ans=models.TextField(max_length=50)
