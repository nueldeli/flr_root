#added file
from django.shortcuts import render
from blog.models import Post

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def organization(request):
	return render(request, 'organization.html')

def all_posts(request):
	post_list = Post.objects.all().order_by('date_created')[:3]
	context = {'post_list' : post_list}
	return render(request, '_include/latest_stories.html', context)