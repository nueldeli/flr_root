from django import forms
from .models import TreeSpeciesData

class AddTreeForm(forms.ModelForm):
	class Meta:
		model = TreeSpeciesData
		fields = ('local_name', 'scientific_name', 'category', 'origin', 'quantity', 'nursery','description', 'remarks', 'tree_species_img')

		widgets = {
			'local_name':forms.TextInput(attrs={'class':'form-control'}),
			'scientific_name':forms.TextInput(attrs={'class':'form-control'}),
			'category':forms.TextInput(attrs={'class':'form-control'}),
			'origin':forms.TextInput(attrs={'class':'form-control'}),
			'quantity':forms.NumberInput(),
			'nursery':forms.TextInput(attrs={'class':'form-control'}),
			'description':forms.Textarea(attrs={'class':'form-control'}),
			'remarks':forms.TextInput(attrs={'class':'form-control'}),
			'tree_species_img':forms.FileInput()
		}

class UpdateTreeForm(forms.ModelForm):
	class Meta:
		model = TreeSpeciesData
		fields = ('local_name', 'scientific_name', 'category', 'origin', 'quantity', 'nursery','description', 'remarks', 'tree_species_img')

		widgets = {
			'local_name':forms.TextInput(attrs={'class':'form-control'}),
			'scientific_name':forms.TextInput(attrs={'class':'form-control'}),
			'category':forms.TextInput(attrs={'class':'form-control'}),
			'origin':forms.TextInput(attrs={'class':'form-control'}),
			'quantity':forms.NumberInput(),
			'nursery':forms.TextInput(attrs={'class':'form-control'}),
			'description':forms.Textarea(attrs={'class':'form-control'}),
			'remarks':forms.TextInput(attrs={'class':'form-control'}),
			'tree_species_img':forms.FileInput()
		}