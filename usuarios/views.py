from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import logout
from usuarios.models import UsuarioDatos


def inicio(request):
    return render_to_response('index.html')

def Registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save()
    	    telefono = request.POST['telefono']
    	    direccion = request.POST['direccion']
    	    usuario = UsuarioDatos()
    	    usuario.usuario = nuevo_usuario
    	    usuario.telefono = telefono
    	    usuario.direccion = direccion
    	    usuario.save()
        return HttpResponseRedirect("/usuarios/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {
        'form': form,
    })


def salir(request):
    logout(request)
    return HttpResponseRedirect('/usuarios/login/')
