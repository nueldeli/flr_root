from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'content')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog title'}),
			'author':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog content'}),
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'content')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog title'}),
			'author':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog content'})
		}