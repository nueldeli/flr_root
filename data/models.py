from django.db import models
from django.urls import reverse

# Create your models here.
class TreeSpeciesData(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	local_name = models.CharField('Local Name', max_length=250)
	scientific_name = models.CharField(max_length=250, null=True)
	category = models.CharField(max_length=250, null=True)
	origin = models.CharField(max_length=250, null=True)
	description = models.TextField(blank=True)
	nursery = models.CharField(max_length=250)
	remark = models.CharField(max_length=250)

	def __str__(self):
		return self.local_name

	def get_absolute_url(self):
		return reverse('data')