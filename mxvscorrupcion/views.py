from django.shortcuts import render
from django.http import Http404
from django.template import loader

from .models import Empresa


# Create your views here.
def empresa(request):
	empresas = Empresa.objects.all()
	context = {
		'empresas':empresas
	}
	return render(request, 'empresa/index.html', context)

def logout(request):
	pass