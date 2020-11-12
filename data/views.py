from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TreeSpeciesData
from .forms import AddTreeForm, UpdateTreeForm
from django.urls import reverse_lazy

all_tree_species = TreeSpeciesData.objects.all()

niah_list = all_tree_species.filter(nursery__icontains='Niah')
sabal_list = all_tree_species.filter(nursery__icontains='Sabal')
semenggoh_list = all_tree_species.filter(nursery__icontains='Semenggoh')

niah_count = niah_list.count()
sabal_count = sabal_list.count()
semenggoh_count = semenggoh_list.count()

# Create your views here.
def data_index(request):
	return render(request, 'data/data_index.html')

def nursery_index(request):
	return render(request, 'data/nursery.html', {'niah_count':niah_count, 'sabal_count':sabal_count, 'semenggoh_count':semenggoh_count})

def sabal_species(request):
	return render(request, 'data/_include/sabal_species.html', {'sabal_list':sabal_list})

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


