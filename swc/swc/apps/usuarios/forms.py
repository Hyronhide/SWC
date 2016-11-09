from django import forms
from django.contrib.auth.models import User 
#from django.forms.widgets import PasswordInput


class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())	
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))	
