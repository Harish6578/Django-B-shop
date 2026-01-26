from django import forms
from .models import ProductImage

class ProductImage(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields=['img','caption']

   