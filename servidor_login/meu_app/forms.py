from django import forms
from .models import Usuario

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'senha']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),     
        }