from django.urls import path
from . import views
from .views import TreeSpeciesView, AddTreeView, SpeciesView, UpdateTreeView, DeleteTreeView

urlpatterns = [
	path('', views.data_index, name='data'),
	path('tree_species/', views.aggregated_sabal),
	path('tree_species/', TreeSpeciesView.as_view(), name='tree_species'),
	path('tree_species_view/<int:pk>', SpeciesView.as_view(), name='tree_species_view'),
	path('add_tree/', AddTreeView.as_view(), name='add_tree'),
	path('tree_species_view/<int:pk>/update', UpdateTreeView.as_view(), name='update_tree'),
	path('tree_species_view/<int:pk>/delete', DeleteTreeView.as_view(), name='delete_tree'),
]