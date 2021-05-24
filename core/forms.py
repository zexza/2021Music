from django import forms
from .models import Producto

#########################
class Prodform(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','portada','precio','cantidad','descipcion','marca','categoria')

