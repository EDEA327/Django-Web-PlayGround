from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCretionFormwithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text="Requerido,254 caracteres como maximo y deber ser válido.")

    class Meta:
        model = User
        files = {'username','email','password1','password2'}

