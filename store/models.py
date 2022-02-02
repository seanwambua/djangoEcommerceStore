from django.conf import settings #making use of the django_allauth plugin
from django.db import models


# Create your models here.
class Item(models.Model):
	title= models.CharField(max_length=100)
	price = models.FloatField()

	#Defining a string method.
	def __str__(self):
		return self.title

class OrderItems(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)

	#Defining a string method.
	def __str__(self):
		return self.title

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	items = models.ManyToManyField(OrderItems)
	startdate = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	#Defining a string method.
	def __str__(self):
		return self.user.username



