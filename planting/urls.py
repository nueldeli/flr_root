from django.urls import path
from . import views
from .views import ProgrammeView, AddProgrammeView, UpdateProgrammeView, DeleteProgrammeView

urlpatterns = [
	path('', views.planting_index, name='planting_index'),
	path('planting_view_programme/', ProgrammeView.as_view(), name='planting_view_programme'),
	path('add_programme/', AddProgrammeView.as_view(), name='add_programme'),
	path('update_programme/<int:pk>/update', UpdateProgrammeView.as_view(), name='update_programme'),
	path('delete_programme/<int:pk>/delete', DeleteProgrammeView.as_view(), name='delete_programme'),
	path('planting_partner/', views.planting_partner_view, name='planting_partner_view'),
]