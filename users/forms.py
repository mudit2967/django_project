from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	phone_number=forms.CharField(max_length=10, help_text='Required.')

	class Meta:
		model=User
		fields=['username','phone_number','password1','password2']