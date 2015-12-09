from django.db import models

# Create your models here.

class Property(models.Model):
	Price = models.IntegerField()
	ContractType = models.CharField(max_length=50)
	Type = models.CharField(max_length=50)
	LocationName= models.CharField(max_length=50)
	Latitude= models.FloatField(max_length=50)
	Longitude= models.FloatField(max_length=50)
	Area= models.CharField(max_length=50)
	FeaturesDesc= models.TextField()
	