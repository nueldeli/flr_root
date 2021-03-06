from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
			'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
		}

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user
