from django import forms
from users.models import Registro

class RegistroForm(forms.ModelForm):    
    class Meta: 
        model = Registro
        fields = ['email','passphrase']