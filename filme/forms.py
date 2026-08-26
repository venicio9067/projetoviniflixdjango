from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False,widget=forms.EmailInput(attrs={'class': 'w-full h-[42px] px-2 text-black'}))


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

