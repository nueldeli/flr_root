from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageFieldFile, FileField 


# Create your models here.
class TreeSpeciesData(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	tree_species_img = models.ImageField('Tree Species Image',null=True, blank=True, upload_to='tree_species_img/')
	local_name = models.CharField('Local Name', max_length=250)
	scientific_name = models.CharField(max_length=250, null=True)
	category = models.CharField(max_length=250, null=True)
	origin = models.CharField(max_length=250, null=True)
	quantity = models.IntegerField('Total', null=True)
	description = models.TextField(blank=True)
	nursery = models.CharField(max_length=250, blank=True)
	remarks = models.CharField(max_length=250, blank=True)

	def __str__(self):
		return self.local_name

	def get_tree_species_img(self):
		if self.tree_species_img and hasattr(self.tree_species_img, 'url'):
			return self.tree_species_img.url
		return ImageFieldFile(instance=None, field=FileField(), name='/media/tree_species_img/tree_species_default.png')

	def get_absolute_url(self):
		return reverse('data')

#Model on planting record
class PlantingRecord(models.Model):
	date_planted = models.DateTimeField()
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
		return reverse('data')
