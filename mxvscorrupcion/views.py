from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponse

from openpyxl import Workbook, load_workbook

from .models import Empresa, Cuestionario, Pregunta, Articulo, Catalogo_Preguntas, Respuestas


# Create your views here.
# def index(request):
# 	user = request.user
# 	if user.is_authenticated:
# 		return redirect('empresa')
# 	else:
# 		return redirect(settings.LOGIN_URL)

def index(request):
	posts = Articulo.objects.all()
	template = 'micrositio/index.html'
	context = {'posts': posts}

	return render(request, template, context)


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
		return render(request, 'empresa/edit-info.html', context)
	else:
		return redirect(settings.LOGIN_URL)


def editInfo(request):
	user = request.user
	if user.is_authenticated:
		empresa = Empresa.objects.get(nombre=user.first_name)
		cuestionario = Cuestionario.objects.get(pk=empresa.cuestionario_id)
		preguntas = cuestionario.preguntas.all()
		print(preguntas[0].reactivo)

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
			group = user.groups.all()[0].name
			if group == 'empresa':
				login(request, user)
				return redirect(settings.LOGIN_REDIRECT_URL, user)
			elif group == 'revisor' :
				login(request, user)
				return redirect('/revisor/', user)
			else :
				login(request, user)
				return redirect('/admin/', user)
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


def articulos(request, slug):
	articulo = get_object_or_404(Articulo, slug=slug)
	template = 'micrositio/post.html'
	context = {
		'post': articulo
	}
	return render(request, template, context)


def revisor(request):
	template = 'revisor/index.html'
	return render(request, template)


def validate(request):
	template = 'revisor/validate.html'
	return render(request, template)

def import_empresas(request):
	wb = load_workbook('mxvscorrupcion/501.xlsx')
	sheet = wb.get_sheet_by_name('Códigos')
	print(sheet)
	row1 = sheet.cell(row=3, column=3)
	print(row1)
	for line in range(9, 45):
		# for col in range(1,3):
		# print(sheet.cell(line, 1).value)
		# print(sheet.cell(line, 2).value)
		# print(sheet.cell(line, 3).value)
		pregunta = Catalogo_Preguntas()
		pregunta.bloque = sheet.cell(row=line, column=1).value
		pregunta.id_reactivo = sheet.cell(row=line, column=2).value
		pregunta.descripcion = sheet.cell(row=line, column=3).value
		pregunta.save()
		respuestas = Respuestas()
		respuestas.opcion = sheet.cell(row=line, column=4).value
		if (respuestas.opcion is None):
			respuestas.opcion = 'N/A'
		respuestas.valor = '0'
		respuestas.catalogo_pregunta = pregunta
		respuestas.save()
		respuestas = Respuestas()
		respuestas.opcion = sheet.cell(row=line, column=5).value
		if (respuestas.opcion is None):
			respuestas.opcion = 'N/A'
		respuestas.valor = '0.5'
		respuestas.catalogo_pregunta = pregunta

		respuestas.save()
		respuestas = Respuestas()
		respuestas.opcion = sheet.cell(row=line, column=6).value
		if (respuestas.opcion is None):
			respuestas.opcion = 'N/A'
		respuestas.valor = '1'
		respuestas.catalogo_pregunta = pregunta

		respuestas.save()

	return HttpResponse(row1.value)
