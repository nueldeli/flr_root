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
	quantity = models.IntegerField(null=True)
	description = models.TextField(blank=True)
	nursery = models.CharField(max_length=250, blank=True)
	remarks = models.CharField(max_length=250, blank=True)

	def __str__(self):
		return self.local_name

	def get_thumbnail(self):
		if self.tree_species_img and hasattr(self.tree_species_img, 'url'):
			return self.tree_species_img
		return ImageFieldFile(instance=None, field=FileField(), name='/media/tree_species_img/tree_species_default.png')

	def get_absolute_url(self):
		return reverse('data')