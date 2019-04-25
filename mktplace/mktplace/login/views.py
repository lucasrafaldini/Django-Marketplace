from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, render_to_response

from .forms.forms import RegistrationForm


def register(request):
    name = 'Cadastro'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect(reverse('login_register_success'))

    else:
        form = RegistrationForm()
    context = {'form': form, 'name': name}

    return render(request, 'registration/register.html', context)


def register_success(request):
    name = 'Cadastrado com sucesso'
    context = {'name': name}
    return render_to_response('registration/success.html', context)
