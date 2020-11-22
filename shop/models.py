from django.contrib.postgres.utils import prefix_validation_error
from django.db import models
from django.core.exceptions import ValidationError






def error_v (value):
    raise ValidationError("fuck %(value)s sdf")

class shop (models.Model):
    company = models.OneToOneField("company",on_delete=models.CASCADE,null=True)
    salessite = models.ForeignKey("salessite",on_delete=models.PROTECT)
    name = models.CharField( max_length=100)
    url=models.URLField( max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="shop_poster", height_field=None, width_field=None, max_length=None ,blank=None,default='new')
    price= models.IntegerField()
    dateone=models.DateTimeField(auto_now_add=True)
    dateupadte=models.DateTimeField(auto_now=True)




    def __str__(self):

        return self.name






class company (models.Model):
    nname = models.CharField(max_length=50)
    site = models.URLField(max_length=200)
    address = models.TextField()
    country = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    # location = LocationField()
    email = models.EmailField( max_length=254)
    Description = models.TextField()

    def __str__(self):
        return self.site









class salessite (models.Model):
    company = models.ForeignKey(company, on_delete=models.PROTECT)
    name = models.CharField( max_length=50)
    site = models.URLField( max_length=200)
    address = models.TextField()
    country = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    mapp =  models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.address

