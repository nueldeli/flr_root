"""from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'"""
from django.shortcuts import render
from .models import Post

def all_posts(request):
	post_list = Post.objects.filter(status='published').order_by('-date_created')
	return render(request, 'blog/index.html', {'post_list':post_list})
