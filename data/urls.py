from django.urls import path
from . import views
from .views import TreeSpeciesView, AddTreeView, SpeciesView, UpdateTreeView, DeleteTreeView

urlpatterns = [
	path('', views.data_index, name='data'),
	path('tree_species/', TreeSpeciesView.as_view(), name='tree_species'),
	path('tree_species_view/<int:pk>', SpeciesView.as_view(), name='tree_species_view'),
	path('add_tree/', AddTreeView.as_view(), name='add_tree'),
	path('tree_species_view/<int:pk>/update', UpdateTreeView.as_view(), name='update_tree'),
	path('tree_species_view/<int:pk>/delete', DeleteTreeView.as_view(), name='delete_tree'),
	path('nursery/', views.nursery_index, name='nursery'),
	path('sabal_species/', views.sabal_species, name='sabal_species'),
	path('semenggoh_species/', views.semenggoh_species, name='semenggoh_species'),
	path('niah_species/', views.niah_species, name='niah_species'),
]