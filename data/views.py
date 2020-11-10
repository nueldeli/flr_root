from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TreeSpeciesData
from .forms import AddTreeForm, UpdateTreeForm
from django.urls import reverse_lazy

# Create your views here.
def data_index(request):
	return render(request, 'data/data_index.html')

class TreeSpeciesView(ListView):
	model = TreeSpeciesData
	template_name = 'data/tree_species.html'
	ordering = ['-date_input']

class SpeciesView(DetailView):
	model = TreeSpeciesData
	template_name = 'data/tree_species_view.html'

class AddTreeView(CreateView):
	model = TreeSpeciesData
	form_class = AddTreeForm
	template_name = 'data/add_tree.html'
	success_url = reverse_lazy('tree_species')

class UpdateTreeView(UpdateView):
	model = TreeSpeciesData
	form_class = UpdateTreeForm
	template_name = 'data/update_tree.html'
	success_url = reverse_lazy('tree_species')

class DeleteTreeView(DeleteView):
	model = TreeSpeciesData
	template_name = 'data/delete_tree.html'
	success_url = reverse_lazy('tree_species')

#def all_posts(request):
	#post_list = Post.objects.filter(status='published').order_by('-date_created')
	#return render(request, 'blog/blog.html', {'post_list':post_list})

def aggregated_sabal(request):
	q = TreeSpeciesData.objects.filter(nursery__icontains='Sabal')
	a = q.count()
	return render(request, 'data/tree_species.html', {'a':a})

