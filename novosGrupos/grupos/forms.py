from django import forms
from .models import Grupo, Artista, Comeback

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'debut', 'resumo']
        widgets = {

            'nome':forms.TextInput(attrs={'placeholder':'Nome do grupo'}),
            'debut':forms.TextInput(attrs={'placeholder':'Debut do grupo'}),
            'resumo':forms.Textarea(attrs={'placeholder':'Resumo do grupo'}),
        }

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'grupo', 'idade', 'genero', 'pais']
        widgets = {

            'nome':forms.TextInput(attrs={'placeholder':'Nome do artista'}),
            'idade':forms.NumberInput(attrs={'placeholder':'Idade do artista'}),
            'pais':forms.TextInput(attrs={'placeholder':'País do artista'}),
        }

class ComebackForm(forms.ModelForm):
    class Meta:
        model = Comeback
        fields = ['nome', 'grupo', 'data', 'views', 'likes', 'deslikes']
        widgets = {

            'nome':forms.TextInput(attrs={'placeholder':'Nome do comeback'}),
            'data':forms.DateInput(attrs={'placeholder':'Data do comeback'}),
            'views':forms.NumberInput(attrs={'placeholder':'Número de views'}),
            'likes':forms.NumberInput(attrs={'placeholder':'Número de likes'}),
            'deslikes':forms.NumberInput(attrs={'placeholder':'Número de deslikes'}),
        }