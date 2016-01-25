from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import auth
# Create your models here.
class paints(models.Model):
    name=models.CharField(max_length=40)
    product_type=models.CharField(max_length=20)
    brand=models.CharField(max_length=20)
    finish_type=models.CharField(max_length=20)
    coverage=models.CharField(max_length=30)
    availability=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    best_for=models.CharField(max_length=10)
    washability=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    eco_friendly=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    durability=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    image=models.CharField(max_length=1000)
    owner=models.ForeignKey('auth.User',related_name='paint')