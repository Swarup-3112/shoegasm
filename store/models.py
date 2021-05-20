from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import SlugField

# Create your models here.

class product(models.Model):

    Category = (
        ( 'Casual' , 'Casual'),
        ( 'Sneaker' , 'Sneaker'),
        ( 'Sport' , 'Sport')
    )

    Gender = (
        ('Men' , 'Men'),
        ('Woman' , 'Woman'),
        ('Both' , 'Both')
    )

    name = models.CharField(max_length=100 , null=True)
    category = models.CharField(max_length=100 , null=True , choices=Category)
    sub_catogery = models.CharField(max_length=100 , null=True)
    price = models.FloatField(null=True)
    color = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, null=True , blank=True , choices=Gender)
    product_img = models.ImageField( null=True , blank=True)

    def __str__(self):
     return self.name

class cart(models.Model):
    product_id = models.ForeignKey(product , on_delete=CASCADE)
    customer = models.ForeignKey(User , on_delete=CASCADE)
    def __str__(self):
         return self.customer.username