from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import AddPostForm, UpdatePostForm
from django.urls import reverse_lazy


#def all_posts(request):
	#post_list = Post.objects.filter(status='published').order_by('-date_created')
	#return render(request, 'blog/blog.html', {'post_list':post_list})

class BlogView(ListView):
	model = Post
	template_name = 'blog/blog.html'
	ordering = ['-date_created']

class BlogPostView(DetailView):
	model = Post
	template_name = 'blog/blog_post.html'

class AddPostView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'blog/add_post.html'

class UpdatePostView(UpdateView):
	model = Post
	form_class = UpdatePostForm
	template_name = 'blog/update_post.html'

	def dispath(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.user != self.request.user:
			raise Http404('You are not allowed to edit this Post')
		return super(UpdatePostView, self).dispatch(request, *args, **kwargs)

class DeletePostView(DeleteView):
	model = Post
	template_name = 'blog/delete_post.html'
	success_url = reverse_lazy('blog')

