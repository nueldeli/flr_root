#added file
from django.shortcuts import render
from blog.models import Post
from blog.views import Blogview
from django.views.generic import ListView

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def organization(request):
	return render(request, 'organization.html')

class LatestStories(ListView):
	model = Post
	template_name = '_include/latest_stories.html'
	ordering = ['-date_created']