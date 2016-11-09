from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from swc.apps.usuarios.forms import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User ##


# Create your views here.
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():#verificacmos si el usuario ya esta authenticado o logueado
		return HttpResponseRedirect('/areas/')#si esta logueado lo redirigimos a la pagina principal
	else: #si no esta authenticado 
		if request.method == "POST":
			formulario = Login_form(request.POST) #creamos un objeto de Loguin_form
			if formulario.is_valid(): #si la informacion enviada es correcta		
				usu= formulario.cleaned_data['usuario'] #guarda informacion ingresada del formulario
				pas= formulario.cleaned_data['clave'] #guarda informacion ingresada del formulario
				usuario = authenticate(username = usu,password = pas)#asigna la autenticacion del usuario
				if usuario is not None and usuario.is_active:#si el usuario no es nulo y esta activo
					login(request,usuario)#se loguea al sistema con la informacion de usuario
					return HttpResponseRedirect('/areas/')#redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form() #creamos un formulario nuevo limpio
		ctx = {'form':formulario, 'mensaje':mensaje}#variable de contexto para pasar info a login.html
		return render_to_response('usuarios/login.html',ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)# funcion de django importda anteriormente
	return HttpResponseRedirect('/')# redirigimos a la pagina principal
		