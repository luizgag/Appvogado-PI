from django import forms
from .models import Advogado, Usuario


class CadastroAdvogadoForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = [
            'nome', 'email', 'sobre', 'telefone', 'endereco',
            'anos_experiencia', 'especialidade'
        ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'email', 'senha'
        ]