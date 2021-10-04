from django import forms
from .models import EmpresaNome

class EmpresaNomeModelForm(forms.ModelForm):
    class Meta:
        model = EmpresaNome
        fields = ['nome', 'cnpj']