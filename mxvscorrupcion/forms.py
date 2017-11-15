from django import forms
from django.forms import Textarea, HiddenInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Perfil, Pregunta_Rechazada

class SignUpForm(UserCreationForm):
    password_random = User.objects.make_random_password(length=14)
    password1 = forms.CharField(label="password", strip=False, widget=HiddenInput(attrs={'value':password_random}))
    password2 = forms.CharField(label="password", strip=False, widget=HiddenInput(attrs={'value':password_random}))
    last_name = forms.CharField(max_length=255, label='Apellidos', required=True)
    email = forms.EmailField(max_length=255, label='Correo Electronico', required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'El correo que intentas registrar ya esta en uso.')
        return email

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('telefono_fijo', 'telefono_celular', 'empresa',)

class Pregunta_Rechazada_Form(forms.ModelForm):

    class Meta:
        model = Pregunta_Rechazada
        fields = ('motivo', 'respuestaPersonalizada','comentarios',)