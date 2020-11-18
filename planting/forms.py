from django import forms
from .models import PlantingRecord

class AddProgrammeForm(forms.ModelForm):
	class Meta:
		model = PlantingRecord
		fields = ('programme_name', 'date_planted', 'programme_img', 'location', 'region', 'area', 'species', 'participants')

		widgets = {
			'date_planted':forms.TextInput(attrs={'class':'form-control'}),
			'programme_name':forms.TextInput(attrs={'class':'form-control'}),
			'programme_img':forms.FileInput(),
			'location':forms.TextInput(attrs={'class':'form-control'}),
			'region':forms.TextInput(attrs={'class':'form-control'}),
			'area':forms.NumberInput(),
			'species':forms.TextInput(attrs={'class':'form-control'}),
			'participants':forms.TextInput(attrs={'class':'form-control'}),

		}

class UpdateProgrammeForm(forms.ModelForm):
	class Meta:
		model = PlantingRecord
		fields = ('programme_name', 'date_planted', 'programme_img', 'location', 'region', 'area', 'species', 'participants')

		widgets = {
			'programme_name':forms.TextInput(attrs={'class':'form-control'}),
			'date_planted':forms.TextInput(attrs={'class':'form-control'}),
			'programme_img':forms.FileInput(),
			'location':forms.TextInput(attrs={'class':'form-control'}),
			'region':forms.TextInput(attrs={'class':'form-control'}),
			'area':forms.NumberInput(),
			'species':forms.TextInput(attrs={'class':'form-control'}),
			'participants':forms.TextInput(attrs={'class':'form-control'}),

		}