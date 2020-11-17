from django.urls import path
from . import views

urlpatterns = [
	path('', views.planting_index, name='planting_index'),
	path('planting_programme/', views.planting_view_programme, name='planting_view_programme'),
	path('planting_partner/', views.planting_partner_view, name='planting_partner_view'),
]