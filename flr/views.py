#added file
from django.shortcuts import render
from blog.models import Post

def home(request):
	post_list = Post.objects.all().order_by('-date_created')[:4]
	context = {'post_list':post_list}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')

def organization(request):
	return render(request, 'organization.html')
