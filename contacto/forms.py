from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.EmailField(label="Correo", required=True)

    contenido = forms.CharField(label="Mensaje",widget=forms.Textarea)