from django.db import models

# Create your models here
class Customer(models.Model):
    customerName=models.CharField(max_length=1000,blank=False)
    customerEmail=models.EmailField(max_length=100,blank=False)
    customerPhone=models.CharField(max_length=100,blank=False)
    
