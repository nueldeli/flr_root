from django.db import models
from django.contrib.auth.models import User                         
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields.files import ImageFieldFile, FileField 

#Status for the blog post
##STATUS_CHOICES = (
	#('draft', 'Draft'),
	#('published', 'Published'),
#)

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE) 
	title = models.CharField('Blog Title', max_length=200)
	slug = models.SlugField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	content = RichTextUploadingField(blank=True)
	#content = models.TextField(blank=True)
	date_updated = models.DateTimeField(auto_now=True)
	thumbnail_img = models.ImageField('Thumbnail', null=True, blank=True, upload_to='thumbnail/')
	#caption_main_img = models.CharField(max_length=250, null=True, blank=True)
	#first_body_img = models.ImageField(null=True, blank=True)
	#caption_first_img = models.CharField(max_length=250, null=True, blank=True)
	#second_body_img = models.ImageField(null=True, blank=True)
	#caption_second_img = models.CharField(max_length=250, null=True, blank=True)

	#status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')

	#class Meta:
		#ordering = ('-date_created',)

	def __str__(self):
		return self.title + " | " + str(self.author)

	def get_thumbnail(self):
		if self.thumbnail_img and hasattr(self.thumbnail_img, 'url'):
			return self.thumbnail_img.url
		return ImageFieldFile(instance=None, field=FileField(), name='/media/thumbnail/flr_default.png')

	def get_absolute_url(self):
		return reverse('blog')


#This function runs when a signal calls it (For slugify-ing the slug)
def slug_generator(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
