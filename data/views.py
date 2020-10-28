from django.shortcuts import render
from django.views.generic import ListView
from .models import TreeSpeciesData

# Create your views here.
def data_index(request):
	return render(request, 'data/data_index.html')

class TreeSpeciesView(ListView):
	model = TreeSpeciesData
	template_name = 'data/tree_species.html'
	ordering = ['-date_input']