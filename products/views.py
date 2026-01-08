from django.shortcuts import render

from .models import Product

# Create your views here.
def productView(request):
    template = 'products/pr'