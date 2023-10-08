from django.shortcuts import render
from django.contrib.auth import views as auth_views
from frontend.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm

# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'index.html')


class UserLoginView(auth_views.LoginView):
  template_name = 'login.html'
  form_class = LoginForm
  success_url = 'accounts/profile/'
