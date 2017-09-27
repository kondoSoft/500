from django.shortcuts import render, redirect
from django.http import Http404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.conf import settings



from .models import Empresa, Cuestionario


# Create your views here.

def empresa(request):
	user = request.user
	empresa = Empresa.objects.get(nombre=user.first_name)
	cuestionario = Cuestionario.objects.get(pk=empresa.cuestionario_id)
	preguntas = cuestionario.preguntas.all()
	empresas = Empresa.objects.all()
	context = {
		'empresas':empresas,
		'empresa': empresa,
		'preguntas': preguntas
	}
	if user.is_authenticated:
		return render(request, 'empresa/index.html', context)
	else:
		return redirect(settings.LOGIN_URL)


def editInfo(request):
	user = request.user
	empresa = Empresa.objects.get(nombre=user.first_name)


	context = {
		'empresa': empresa
	}
	if user.is_authenticated:
		return render(request, 'empresa/edit-info.html', context)
	else:
		return redirect(settings.LOGIN_URL)	


def loginUser(request):
	method = request.method
	if method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			context = {
			'user': user
			}
			return redirect(settings.LOGIN_REDIRECT_URL, user)
		else:
			return render(request, 'empresa/login.html', {'error': True})
	else:
		return render(request,'empresa/login.html' )


def register(request):
	return render(request, 'empresa/register.html')
