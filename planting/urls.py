from django.urls import path
from . import views
from .views import ProgrammeView, AddProgrammeView, UpdateProgrammeView, DeleteProgrammeView, CartView, CartSpeciesView, AddCartView, UpdateCartView, DeleteCartView

urlpatterns = [
	path('', views.planting_index, name='planting_index'),
	path('planting_view_programme/', ProgrammeView.as_view(), name='planting_view_programme'),
	path('add_programme/', AddProgrammeView.as_view(), name='add_programme'),
	path('update_programme/<int:pk>/update', UpdateProgrammeView.as_view(), name='update_programme'),
	path('delete_programme/<int:pk>/delete', DeleteProgrammeView.as_view(), name='delete_programme'),
	path('planting_partner/', CartView.as_view(), name='planting_partner_view'),
	path('cart_species_view/<int:pk>', CartSpeciesView.as_view(), name='cart_species_view'),
	path('add_cart_species/', AddCartView.as_view(), name='add_cart'),
	path('update_cart_species/<int:pk>/', UpdateCartView.as_view(), name='update_cart'),
	path('delete_cart_species/<int:pk>/', DeleteCartView.as_view(), name='delete_cart'),
	path('update_item/', views.updateItem, name='update_item')
]