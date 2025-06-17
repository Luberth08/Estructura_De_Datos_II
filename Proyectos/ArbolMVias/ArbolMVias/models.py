from django import forms

class RegistroForm(forms.Form):
    id_reg = forms.IntegerField(label='ID')
    nombre = forms.CharField(label='Nombre', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    telefono = forms.CharField(label='Teléfono', max_length=15)