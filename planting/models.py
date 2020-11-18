from django.db import models
from django.urls import reverse
from datetime import datetime

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