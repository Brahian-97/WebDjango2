from dataclasses import field, fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class form_estudiantes(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'primer nombre'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'apellido'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'contraseña'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']
        help_texts = {k: "" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Vieja contraseña", widget=forms.PasswordInput(attrs={'placeholder':'Vieja contraseña'}))
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput(attrs={'placeholder':'Nueva contraseña'}))
    new_password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput(attrs={'placeholder':'Confirma contraseña'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        help_texts = {k: "" for k in fields}

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()