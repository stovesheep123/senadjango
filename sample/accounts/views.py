from django.shortcuts import render
from django.contrib.auth import login 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:home")

    def __format__(self, form):
        response = super(). form_valid(form)
        login(self.request, self.object)
        return response

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/home.html"