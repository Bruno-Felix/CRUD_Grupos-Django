from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'debut', 'resumo']
        widgets = {

            'nome':forms.TextInput(attrs={'placeholder':'Nome do grupo'}),
            'debut':forms.TextInput(attrs={'placeholder':'Ano de debut do grupo'}),
            'resumo':forms.Textarea(attrs={'placeholder':'Resumo do grupo'}),
        }