from django.db import models

# Create your models here.

class Customer(models.Model):
	name= models.CharField(max_length=100)
	mobileNumber= models.IntegerField()
	address= models.CharField(max_length=100)


	def __str__(self):
		return self.name