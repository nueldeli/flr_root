from django.shortcuts import render

# Create your views here.
def planting_index(request):
	return render(request, 'planting/planting_index.html')

def planting_view_programme(request):
	return render(request, 'planting/planting_view_programme.html')

def planting_partner_view(request):
	return render(request, 'planting/planting_partner_view.html')