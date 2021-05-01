from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Event, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'nome', 'telefone',
                    'minicurriculo', 'site', 'rede_social', 'eh_palestrante', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event)
