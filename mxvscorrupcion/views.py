from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


from openpyxl import Workbook, load_workbook

from .models import Empresa, Cuestionario, Pregunta, Articulo, Catalogo_Preguntas, Respuestas, Sectores, Paises, Fuentes


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
	return render(request, 'empresa/index.html')

# def editInfo(request):
# 	user = request.user
# 	if user.is_authenticated:
# 		empresa = Empresa.objects.get(nombre=user.first_name)
# 		cuestionario = Cuestionario.objects.get(pk=empresa.cuestionario_id)
# 		preguntas = cuestionario.preguntas.all()
# 		print(preguntas[0].reactivo)

# 		context = {
# 			'empresa': empresa,
# 			'preguntas': preguntas
# 		}
# 		return render(request, 'empresa/edit-info.html', context)
# 	else:
# 		return redirect(settings.LOGIN_URL)


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
	user = request.user
	if user.is_authenticated:
		template = 'revisor/index.html'
		return render(request, template)
	else:
		return redirect(settings.LOGIN_URL)


def validate(request):
	template = 'revisor/validate.html'
	return render(request, template)

def glosario(request):
	if request.method == 'GET':
		data = serializers.serialize("json", Glosario.objects.all())
		return HttpResponse(data)

def fuentes(request):
	if request.method == 'GET':
		data = serializers.serialize("json", Fuentes.objects.all())
		return HttpResponse(data, content_type="application/json")

def import_empresas(request):
	wb = load_workbook('mxvscorrupcion/501.xlsx')
	sheet = wb.get_sheet_by_name('Códigos')
	print(sheet)
	row1 = sheet.cell(row=3, column=3)
	print(row1)
	for line in range(9, 45):
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

def getSector(sector):
	print('getSector ', sector)
	sector = Sectores.objects.filter(nombre=sector.strip())[0]
	return sector

def getCountry(country):
	country = Paises.objects.filter(pais=country)[0]
	return country

def getQuestion(qid):
	print('getQuestion', qid)
	if qid == 'IC_13C':
		qid = 'IC_13A'
	return Catalogo_Preguntas.objects.filter(id_reactivo=qid)[0]

def getAnswersByQid(qid):
	return Respuestas.objects.filter(catalogo_pregunta__pk=qid)


def import_empresas_final(request):
	wb = load_workbook('mxvscorrupcion/501.xlsx')
	sheet = wb.get_sheet_by_name('BD c valores COMP')
	print(sheet)
	row1 = sheet.cell(row=3, column=3)
	print(row1)
	# get questions ids
	# for line in range(9, 45):
	question_id_ary = []
	question_answer = []
	for question in range(7, 43):
		current_id = sheet.cell(row=1, column=question).value
		question_id_ary.append(current_id)

	# get client
	for client_Key in range(3, 502):
		client_data = {}
		client_answers = []
	# for client in range(3, 502):
		# for data in range(1, 6):

		name = sheet.cell(row=client_Key, column=2).value
		sector = sheet.cell(row=client_Key, column=3).value
		pais = sheet.cell(row=client_Key, column=4).value
		website_corporativo = sheet.cell(row=client_Key, column=5).value
		website_integridad = sheet.cell(row=client_Key, column=6).value

		print('name ', name)
		print('sector ', sector)
		client = Empresa()
		client.nombre = name
		client.sector = getSector(sector)
		client.pais = getCountry(pais)
		client.website_corporativo = website_corporativo
		client.website_integridad = website_integridad
		client.save()

		cuestionario = Cuestionario()
		print(dir(cuestionario))
		print(client.pk)

		for question in range(7, 43):
			current_answer = sheet.cell(row=client_Key, column=question).value
			question_answer.append(current_answer)
			qindex = question-7
			print(question_id_ary[qindex])



			question_id = question_id_ary[qindex]
			if question_id != 'IC_15A' and question_id != 'IC_16A' and question_id != 'IC_19A' and question_id != 'IC_22A' and question_id != 'IC_23A':
				question = getQuestion(question_id)
				answers = getAnswersByQid(question.pk)
				selected_answer = answers.filter(valor = current_answer)[0]
				# try:
				preguntaObj = Pregunta()
				preguntaObj.reactivo = question
				preguntaObj.respuesta = selected_answer
				preguntaObj.save()
				cuestionario.Empresa = client
				cuestionario.save()
				cuestionario.preguntas.add(preguntaObj)
				cuestionario.save()
				# except:
				# 	print('''pregunta couldn't be added''')
				# 	pass




			res = [question_id_ary, question_answer]


	return HttpResponse(res)

@csrf_exempt
def send_email(request):
	method = request.method
	if method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		result = send_mail(
			'Haz recibido un correo de ' + name + ' | Contacto Integridad Corporativa',
			message,
			email,
			['contacto@integridadcorporativa500.mx'],
			fail_silently=False
		)
		if result:
			return JsonResponse({'ok': True})
			
	# elif method == 'GET':
	# 	return HttpResponse('Listo')


