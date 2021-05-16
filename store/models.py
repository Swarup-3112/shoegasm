from django.db import models

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