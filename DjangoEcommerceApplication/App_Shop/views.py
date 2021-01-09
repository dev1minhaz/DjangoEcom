from django.shortcuts import render

# import views
from django.views.generic import ListView, DetailView

# models
from .models import Product

# Create your views here.


class Home(ListView):
    model = Product
    template_name = "App_Shop/home.html"
