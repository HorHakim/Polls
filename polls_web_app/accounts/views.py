from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomSignUpForm
from django.contrib.auth.views import LoginView

# Create your views here.
def home(request):
	return render(request, "accounts/home.html", {})

class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'
  next_page = 'polls:index'

  def form_invalid(self, form):
      messages.error(self.request, "Le nom d'utilisateur ou le mot de passe est invalide")
      return super().form_invalid(form)


def logout_account(request):
    logout(request)
    return redirect("accounts:home")

def signup(request):
	if request.method == "GET":
		signup_form = CustomSignUpForm()
		
	elif request.method == "POST":
		signup_form = CustomSignUpForm(request.POST)
		if signup_form.is_valid():
			user = signup_form.save()
			login(request, user)
			return redirect("polls:index")


	return render(request, "accounts/signup.html", {"signup_form" : signup_form})
