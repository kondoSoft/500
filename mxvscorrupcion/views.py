from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.conf import settings

from .models import Empresa, Cuestionario, Pregunta


# Create your views here.
def index(request):
	user = request.user
	if user.is_authenticated:
		return redirect('empresa')
	else:
		return redirect(settings.LOGIN_URL)


def empresa(request):
	user = request.user
	if user.is_authenticated:
		empresa = Empresa.objects.get(nombre=user.first_name)
		cuestionario = Cuestionario.objects.get(pk=empresa.cuestionario_id)
		preguntas = cuestionario.preguntas.all()
		empresas = Empresa.objects.all()
		context = {
			'empresas':empresas,
			'empresa': empresa,
			'preguntas': preguntas
		}
		return render(request, 'empresa/index.html', context)
	else:
		return redirect(settings.LOGIN_URL)


def editInfo(request):
	user = request.user
	if user.is_authenticated:
		empresa = Empresa.objects.get(nombre=user.first_name)
		cuestionario = Cuestionario.objects.get(pk=empresa.cuestionario_id)
		preguntas = cuestionario.preguntas.all()

		context = {
			'empresa': empresa,
			'preguntas': preguntas
		}
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
			return redirect(settings.LOGIN_REDIRECT_URL, user)
		else:
			return render(request, 'empresa/login.html', {'error': True})
	else:
		return render(request,'empresa/login.html' )


def register(request):
	return render(request, 'empresa/register.html')


def modifyAnswer(request, pk):
	if request.method == 'GET' :
		pregunta = Pregunta.objects.get(pk=pk)
		pregunta = pregunta.__dict__
		respuesta = pregunta['respuesta']
		return HttpResponse(respuesta)
	else:
		question_id = request.POST.get('pregunta_id')
		pregunta = Pregunta.objects.get(pk=question_id)
		pregunta.respuesta = request.POST.get('respuesta')
		pregunta.save()
		return redirect('edit-info')









