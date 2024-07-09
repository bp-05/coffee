from django import forms
from coffeeApp.models import CoffeeForm


class FormCoffee(forms.ModelForm):
    class Meta:
        model = CoffeeForm
        fields = ['nombre', 'correo', 'tipo_solicitud', 'mensaje']
    

