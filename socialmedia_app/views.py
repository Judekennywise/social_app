from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView, View
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .models import Post, Like, Comment

# Create your views here.


class RegistrationFormView(FormView):
	form_class = SignUpForm
	template_name = 'register.html'

	def form_valid(self, form):
		user = form.register()
		user.save()
		return HttpResponseRedirect(reverse_lazy('core:login'))

class LoginFormView(View):
	form_class = LoginForm
	template_name = 'login.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, context={'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.login_user(self.request)
			if user is not None:
				login(self.request, user)
				return HttpResponseRedirect(reverse_lazy('home'))

		return render(request, self.template_name, context={'form': form})

class LogoutView(View):
	def get(self, request):
		logout(self.request)
		return redirect('login')

def home(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, 'home.html', context)





