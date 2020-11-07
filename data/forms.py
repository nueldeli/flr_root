from django import forms
from .models import TreeSpeciesData

class AddTreeForm(forms.ModelForm):
	class Meta:
		model = TreeSpeciesData
		fields = ('local_name', 'scientific_name', 'category', 'origin', 'quantity', 'description', 'remarks')

		widgets = {
			'local_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Local Name'}),
			'scientific_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scientific Name'}),
			'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
			'origin':forms.TextInput(attrs={'class':'form-control','placeholder':'Origin'}),
			'quantity':forms.NumberInput()
			'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descriptions'}),
			'remarks':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Remarks'})
		}