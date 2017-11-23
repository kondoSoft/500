from django import forms
from django.forms import Textarea, HiddenInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Perfil, Pregunta_Rechazada, Empresa

class SignUpForm(UserCreationForm):
    password_random = User.objects.make_random_password(length=14)
    password1 = forms.CharField(label="password", strip=False, widget=HiddenInput(attrs={'value':password_random}))
    password2 = forms.CharField(label="password", strip=False, widget=HiddenInput(attrs={'value':password_random}))
    last_name = forms.CharField(max_length=255, label='Apellidos', required=True)
    email = forms.EmailField(max_length=255, label='Correo Electrónico', required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        help_texts = {
            'username': 'Obligatorio. Longitud máxima 150 caracteres alfanuméricos. Letras, dígitos y @/./+/-/_ únicamente. Ojo no usar caracteres especiales (tildes o acentos).',
        }

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
    telefono_fijo = forms.CharField(max_length=10, label='Teléfono fijo:')
    telefono_celular = forms.CharField(max_length=10, label='Teléfono celular:')
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.order_by('nombre'))
    extension = forms.CharField(max_length=5, label='Ext.', required=False)
    class Meta:
        model = Perfil
        fields = ('telefono_fijo',  'extension', 'telefono_celular', 'empresa',)

class Pregunta_Rechazada_Form(forms.ModelForm):
    respuestaPersonalizada = forms.CharField(label='Respuesta personalizada')
    class Meta:
        model = Pregunta_Rechazada
        fields = ('motivo', 'respuestaPersonalizada','comentarios',)


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups', 'is_staff', 'is_active', 'is_superuser', 'date_joined',]

