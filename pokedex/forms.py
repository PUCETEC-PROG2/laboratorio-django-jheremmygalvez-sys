from django import forms
from .models import Pokemon, Trainer     

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"
        labels = {
            'name': 'Nombre del Pokémon',
            'type': 'Tipo de Pokémon',
            'weight': 'Peso del Pokémon (kg)',
            'height': 'Altura del Pokémon (kg)',
            'picture': 'Foto del Pokémon ',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class TrainerForm(forms.ModelForm):
        class Meta:
            model = Trainer
            fields = '__all__'
            labels = {
            'name': "Nombre:",
            'last_name': "Apellido:",
            'level': "Nivel:",
            'birth': "Fecha de nacimiento:",
            'picture' : "Fotografia",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'level': forms.NumberInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}), 
            "trainer": forms.Select(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': "font-family: 'Momo Trust Display', sans-serif; font-weight: 400; font-style: normal;"}),
        }
        