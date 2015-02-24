from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader, Context
from sistema.forms import *
from sistema.models import *
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib import auth
from django.conf import settings
import os
from os import path
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# Cadastrar, editar e excluir pessoas
def cadastro_pessoa(request):
	if request.method == 'GET':
		pessoa_form = PessoaForm()
	if request.method == 'POST':
		pessoa_form = PessoaForm(request.POST)
		if pessoa_form.is_valid():
			pessoa_form.save()
			sucesso = True
			return HttpResponseRedirect('/cadastro_pessoa/')
		else:
			dados_incorretos = True
			return render(request, 'cadastro_pessoa.html', locals())
	return render(request, 'cadastro_pessoa.html', locals())

def editar_pessoa(request, id_pessoa):
	objeto = Pessoa.objects.get(id = id_pessoa)
	if request.method == 'GET':
		pessoa_form = PessoaForm(instance = objeto)
	if request.method == 'POST':
		pessoa_form = PessoaForm(request.POST,instance = objeto)
		if pessoa_form.is_valid():
			pessoa_form.save()
			sucesso = True
			return HttpResponseRedirect('/editar_pessoa/%s' %id_pessoa)
		else:
			dados_incorretos = True
			return render(request, 'editar_pessoa.html', locals())
	return render(request, 'editar_pessoa.html', locals())

def visualizar_pessoas (request):
    pessoas = Pessoa.objects.all()
    return render(request, 'visualizar_pessoas.html', locals())

def excluir_pessoa(request, id_pessoa):
	objeto = Pessoa.objects.get(id = id_pessoa)
	objeto.delete()
	messages.success(request, 'O cadastro foi deletado')
	return HttpResponseRedirect('/visualizar_pessoas/')

def home(request):
	return render(request, 'home.html', locals())

def login(request):
	login_incorreto = False
	if request.method == 'POST':
		usuario = request.POST.get("username")
		senha = request.POST.get("password")
		user = authenticate(username=usuario, password=senha)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/home/')
		else:
			login_incorreto = True
			return render(request, 'login.html', locals())
	else:
		return render(request, 'login.html', locals())

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login/')