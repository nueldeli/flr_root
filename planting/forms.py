from django import forms
from .models import PlantingRecord, CartSpecies

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

class AddCartForm(forms.ModelForm):
	class Meta:
		model = CartSpecies
		fields = ('cart_local_name', 'cart_scientific_name', 'cart_species_img', 'cart_species_descriptions', 'cart_species_category', 'cart_species_total')

		widgets = {
			'cart_local_name':forms.TextInput(attrs={'class':'form-control'}),
			'cart_scientific_name':forms.TextInput(attrs={'class':'form-control'}),
			'cart_species_img':forms.FileInput(),
			'cart_species_descriptions':forms.Textarea(attrs={'class':'form-control'}),
			'cart_species_category':forms.TextInput(attrs={'class': 'form-control'}),
			'cart_species_total':forms.NumberInput(),
		}


class UpdateCartForm(forms.ModelForm):
	class Meta:
		model = CartSpecies
		fields = ('cart_local_name', 'cart_scientific_name', 'cart_species_img', 'cart_species_descriptions', 'cart_species_category', 'cart_species_total')

		widgets = {
			'cart_local_name':forms.TextInput(attrs={'class':'form-control'}),
			'cart_scientific_name':forms.TextInput(attrs={'class':'form-control'}),
			'cart_species_img':forms.FileInput(),
			'cart_species_descriptions':forms.Textarea(attrs={'class':'form-control'}),
			'cart_species_category':forms.TextInput(attrs={'class': 'form-control'}),
			'cart_species_total':forms.NumberInput(),
		}