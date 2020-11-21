from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import PlantingRecord, CartSpecies, Order
from .forms import AddProgrammeForm, UpdateProgrammeForm, AddCartForm, UpdateCartForm
from django.urls import reverse_lazy
from django.http import JsonResponse
import json

def planting_index(request):
	return render(request, 'planting/planting_index.html')
	
#Planting programme view.
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

#Cart Species view
class CartView(ListView):
	model = CartSpecies
	template_name = 'planting/planting_partner_view.html'
	ordering = ['-date_created_cart']

class CartSpeciesView(DetailView):
	model = CartSpecies
	template_name = 'planting/cart_species_view.html'

class AddCartView(CreateView):
	model = CartSpecies
	form_class = AddCartForm
	template_name = 'planting/add_cart.html'
	success_url = reverse_lazy('planting_partner_view')

class UpdateCartView(UpdateView):
	model = CartSpecies
	form_class = UpdateCartForm
	template_name = 'planting/update_cart.html'
	success_url = reverse_lazy('planting_partner_view')

class DeleteCartView(DeleteView):
	model = CartSpecies
	template_name = 'planting/delete_cart.html'
	success_url = reverse_lazy('planting_partner_view')

def planting_cart(request):
	if request.user.is_authenticated:
		partner = request.user.partner
		order, created = Order.objects.filter(partner=partner, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
	return render(request, 'planting/planting_cart.html', {'items':items})

def updateItem(request):
	data = json.loads(request.body)
	speciesId = data['speciesId']
	action = data['action']

	print('Action', action)
	print('speciesId', speciesId)
	return JsonResponse('Item was added', safe=False)





