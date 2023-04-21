from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email_address(self):
        email = self.cleaned_data.get('email_address')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Sorry user with this email address already exists')
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if Profile.objects.filter(phone = phone).exists():
            raise forms.ValidationError('Sorry user with this phone number already exists')
        return phone
    
class LoginForm(forms.Form):
	email_or_phone = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	


	def clean_email_or_phone(self):
		erf = self.cleaned_data.get('email_or_phone').strip()
		if not(User.objects.filter(email = erf).exists() or Profile.objects.filter(phone=erf).exists()):	
			raise forms.ValidationError('Oops! Sorry, account does not exist')
		return erf

	def get_username(self):
		erf = self.cleaned_data.get('email_or_phone').strip()
		username = None
		if User.objects.filter(email = erf).exists():
			username = User.objects.get(email=erf).username
		elif Profile.objects.filter(phone=erf).exists():
			username = Profile.objects.get(phone=erf).user.username
		return username


	def login_user(self, request):
		username = self.get_username()
		password = self.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		return user
