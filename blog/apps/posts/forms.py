from django import forms

from .models import Comentario, Post


class Formulario_Modificacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("texto",)
        

class Form_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "titulo",
            "cuerpo",
            "imagen",
            "categoria_post",
        )
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria_post': forms.Select(attrs={'class': 'form-control'}),
        }