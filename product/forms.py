from django.forms import forms, ModelForm,NumberInput,\
    ChoiceField, TextInput, Textarea, CheckboxInput

from .models import Variant, ProductVariantPrice


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductForm(ModelForm):
    class Meta:
        model = ProductVariantPrice
        # fields = ["customer","product"]
        fields = '__all__'

