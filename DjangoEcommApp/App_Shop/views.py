from django.shortcuts import render


# import views
from django.views.generic import ListView, DetailView

# models
from .models import Product

# mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Home(ListView):
    model = Product
    template_name = "App_Shop/home.html"


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "App_Shop/product_detail.html"
