from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from datetime import datetime
from django.db.models.fields.files import ImageFieldFile, FileField 

# Create your models here.
class PlantingRecord(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	date_planted = models.CharField(max_length=250)
	programme_name = models.CharField(max_length=250)
	programme_img = models.ImageField('Programme Image', null=True, blank=True, upload_to='programme_img/')
	location = models.CharField(max_length=250)
	region = models.CharField(max_length=250)
	area = models.FloatField()
	species = models.CharField(max_length=255)
	participants = models.CharField(max_length=250)

	def __str__(self):
		return self.programme_name

	def get_programme_img(self):
		if self.programme_img and hasattr(self.programme_img, 'url') :
			return self.programme_img.url
		return ImageFieldFile(instance=None, field=FileField(), name='/media/programme_img/programme_img_default.png')

	def get_absolute_url(self):
		return reverse('planting_index')

class CartSpecies(models.Model):
	date_created_cart = models.DateTimeField(auto_now_add=True)
	cart_local_name = models.CharField('Local Name', max_length=250)
	cart_scientific_name = models.CharField('Scientific Name', max_length=250)
	cart_species_img = models.ImageField('Species Image', null=True, blank=True, upload_to='cart_species_img/')
	cart_species_descriptions = models.TextField('Descriptions', blank=True, null=True)
	cart_species_category = models.CharField('Category', max_length=250)
	cart_species_total = models.IntegerField('Total', null=True)

	def __str__(self):
		return self.cart_local_name

	def get_cart_img(self):
		if self.cart_species_img and hasattr(self.cart_species_img, 'url') :
			return self.cart_species_img.url
		return ImageFieldFile(instance=None, field=FileField(), name='/media/cart_species_img/cart_img_default.png')

	def get_absolute_url(self):
		return reverse('planting_partner_view')

class Partner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=250, null=True)
	email = models.CharField(max_length=250, null=True)
	organization = models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	species = models.ForeignKey(CartSpecies, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added= models.DateTimeField(auto_now_add=True)