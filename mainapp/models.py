from django.db import models
from datetime import date

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    
    
    
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField(default=date.today)