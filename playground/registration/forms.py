from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCretionFormwithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text="Requerido,254 caracteres como maximo y deber ser válido.")

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado pruebe con otro por favor")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','bio','link')
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3','rows':3,'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'Enlace'})

        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required = True, help_text="Requerido,254 caracteres como maximo y deber ser válido.")

    class Meta:
        model = User #Ya tiene sus validaciones internas
        fields = ['email']
        #! la unica forma de poner widgets sin cargarte las validaciones de User
        #! Es poniendo los widgets en tiempo de ejecución osea en la vista.
        #! Ojo con la validacion del correo que no debe existir antes en la base datos.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        #* el primer if es para saber si el email cambió
        if 'email' in self.changed_data:
            #* Pra saber si el nuevo email ya existía.
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado pruebe con otro por favor")
        return email



