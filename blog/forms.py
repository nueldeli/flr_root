from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'slug','content', 'thumbnail_img')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog title'}),
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slug is automatically generated. It\'s OK to leave it empty'}),
			#'author':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog content'}),
			'thumbnail_img':forms.FileInput
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'slug', 'content','thumbnail_img')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog title'}),
			'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slug is automatically generated. It\'s OK to leave it empty'}),
			#'author':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog content'}),
			'thumbnail_img':forms.FileInput
		}