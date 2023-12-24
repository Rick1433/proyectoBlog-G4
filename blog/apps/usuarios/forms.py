from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioRegistro(UserCreationForm):
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control-registro'}),
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control-registro'}))
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control-registro'}),
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control-registro'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
