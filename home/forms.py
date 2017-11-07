from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password','first_name','last_name']



class productForm(forms.Form):
	price = forms.IntegerField()
	company = forms.CharField(max_length=100)
	image = forms.ImageField()





