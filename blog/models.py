from django.db import models

# Create your models here.
class Blog(models.Model):
	author = models.CharField('Blog Author', max_length=120)
	title = models.CharField('Blog Title', max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)
	content = models.TextField(blank=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title