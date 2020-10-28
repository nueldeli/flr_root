from django.urls import path
from . import views
from .views import TreeSpeciesView

urlpatterns = [
	path('', views.data_index, name='data'),
	path('tree_species/', TreeSpeciesView.as_view(), name='tree_species'),
]