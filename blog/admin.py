from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'slug', 'status', 'date_created')
	list_filter = ('status',)
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Post, PostAdmin)