from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.TextField()
    email=models.EmailField()
    mobile=models.TextField()

