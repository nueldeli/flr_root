from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PlantingRecord
from .forms import AddProgrammeForm, UpdateProgrammeForm
from django.urls import reverse_lazy

# Create your views here.
def planting_index(request):
	return render(request, 'planting/planting_index.html')

class ProgrammeView(ListView):
	model = PlantingRecord
	template_name = 'planting/planting_view_programme.html'
	ordering = ['-date_planted']

class AddProgrammeView(CreateView):
	model = PlantingRecord
	form_class = AddProgrammeForm
	template_name = 'planting/add_programme.html'
	success_url = reverse_lazy('planting_view_programme')

class UpdateProgrammeView(UpdateView):
	model = PlantingRecord
	form_class = UpdateProgrammeForm
	template_name = 'planting/update_programme.html'
	success_url = reverse_lazy('planting_view_programme')

class DeleteProgrammeView(DeleteView):
	model = PlantingRecord
	template_name = 'planting/delete_programme.html'
	success_url = reverse_lazy('planting_view_programme')

def planting_partner_view(request):
	return render(request, 'planting/planting_partner_view.html')

