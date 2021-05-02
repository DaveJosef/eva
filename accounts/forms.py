from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = forms.UserChangeForm.Meta.fields


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + \
            ('nome', 'email', 'telefone', 'eh_palestrante',
             'site', 'minicurriculo', 'rede_social',)
