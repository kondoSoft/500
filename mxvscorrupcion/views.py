from django.shortcuts import render, redirect
from django.http import Http404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.conf import settings



from .models import Empresa


# Create your views here.

def index(request):
	return redirect(settings.LOGIN_URL)

def empresa(request):
	user = request.user
	if user.is_authenticated:
		empresas = Empresa.objects.all()
		context = {
			'empresas':empresas,
			'user':user
		}
		return render(request, 'empresa/index.html', context)
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